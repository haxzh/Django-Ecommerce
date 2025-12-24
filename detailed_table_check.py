import os
import django
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.db import connection
from core.models import Item

print("="*80)
print("DETAILED TABLE STRUCTURE CHECK")
print("="*80)

# Check core_item table structure
print("\nCORE_ITEM TABLE STRUCTURE:")
print("-"*80)
with connection.cursor() as cursor:
    cursor.execute("DESCRIBE core_item")
    columns = cursor.fetchall()
    for col in columns:
        print(f"  {col[0]:20s} {col[1]:20s} NULL:{col[2]:5s} Key:{col[3]:5s} Default:{str(col[4]):10s}")

# Check if there are duplicate or wrong columns
print("\nMODEL FIELD EXPECTATIONS:")
print("-"*80)
for field in Item._meta.fields:
    print(f"  {field.name:20s} -> DB Column: {field.column:20s} Type: {field.get_internal_type()}")

# Check for data issues
print("\nDATA CHECK:")
print("-"*80)
with connection.cursor() as cursor:
    cursor.execute("SELECT COUNT(*) FROM core_item")
    count = cursor.fetchone()[0]
    print(f"  Total items in database: {count}")
    
    if count > 0:
        cursor.execute("SELECT id, title, category_id FROM core_item LIMIT 5")
        print("\n  Sample items:")
        for row in cursor.fetchall():
            print(f"    ID: {row[0]}, Title: {row[1]}, Category ID: {row[2]}")

# Check for orphaned columns
print("\nEXTRA COLUMNS CHECK:")
print("-"*80)
expected_columns = [field.column for field in Item._meta.fields]
with connection.cursor() as cursor:
    cursor.execute("DESCRIBE core_item")
    actual_columns = [col[0] for col in cursor.fetchall()]
    
    extra = set(actual_columns) - set(expected_columns)
    missing = set(expected_columns) - set(actual_columns)
    
    if extra:
        print(f"  ⚠ EXTRA columns in database (not in model): {extra}")
    if missing:
        print(f"  ✗ MISSING columns in database: {missing}")
    if not extra and not missing:
        print(f"  ✓ All columns match the model definition")

# Check other core tables
print("\nOTHER CORE TABLES:")
print("-"*80)
with connection.cursor() as cursor:
    cursor.execute("SHOW TABLES LIKE 'core_%'")
    tables = [row[0] for row in cursor.fetchall()]
    for table in sorted(tables):
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        print(f"  {table:30s} {count:5d} records")

# Check foreign key constraints
print("\nFOREIGN KEY CONSTRAINTS:")
print("-"*80)
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT 
            TABLE_NAME,
            COLUMN_NAME,
            CONSTRAINT_NAME,
            REFERENCED_TABLE_NAME,
            REFERENCED_COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE 
            TABLE_SCHEMA = DATABASE()
            AND TABLE_NAME LIKE 'core_%'
            AND REFERENCED_TABLE_NAME IS NOT NULL
    """)
    constraints = cursor.fetchall()
    if constraints:
        for constraint in constraints:
            print(f"  {constraint[0]}.{constraint[1]} -> {constraint[3]}.{constraint[4]}")
    else:
        print("  ⚠ No foreign key constraints found")

print("\n" + "="*80)
