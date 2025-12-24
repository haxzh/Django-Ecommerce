import os
import django
from dotenv import load_dotenv

# Load .env first
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.db import connection

print("Checking core_item table structure...\n")

# Check current structure
with connection.cursor() as cursor:
    cursor.execute("DESCRIBE core_item")
    columns = cursor.fetchall()
    print("Current columns in core_item:")
    for col in columns:
        print(f"  - {col[0]} ({col[1]})")
    
    # Check if category_id exists
    column_names = [col[0] for col in columns]
    
    if 'category_id' not in column_names:
        print("\n⚠ Missing category_id column! Adding it now...\n")
        
        # Add the category_id column
        cursor.execute("""
            ALTER TABLE core_item 
            ADD COLUMN category_id int NOT NULL AFTER discount_price
        """)
        
        # Add foreign key constraint
        cursor.execute("""
            ALTER TABLE core_item 
            ADD CONSTRAINT core_item_category_id_fk 
            FOREIGN KEY (category_id) REFERENCES core_category(id)
        """)
        
        print("✓ Added category_id column with foreign key constraint")
        
        # Verify
        cursor.execute("DESCRIBE core_item")
        columns = cursor.fetchall()
        print("\nUpdated columns in core_item:")
        for col in columns:
            print(f"  - {col[0]} ({col[1]})")
    else:
        print("\n✓ category_id column already exists")

print("\n✅ Table structure fixed!")
