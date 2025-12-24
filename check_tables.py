import os
import django
from dotenv import load_dotenv

# Load .env first
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.db import connection
from django.apps import apps

print("Checking core app tables...\n")

# Get all models from core app
core_app = apps.get_app_config('core')
models = core_app.get_models()

print(f"Models in core app: {[m.__name__ for m in models]}\n")

# Check which tables exist
with connection.cursor() as cursor:
    cursor.execute("SHOW TABLES LIKE 'core_%'")
    tables = [row[0] for row in cursor.fetchall()]
    print(f"Tables found in database: {tables}\n")
    
    print("Detailed table list:")
    cursor.execute("SHOW TABLES")
    all_tables = [row[0] for row in cursor.fetchall()]
    for table in sorted(all_tables):
        print(f"  - {table}")

# Try to query each model
print("\nModel status:")
for model in models:
    try:
        count = model.objects.count()
        print(f"✓ {model.__name__}: {count} records")
    except Exception as e:
        print(f"✗ {model.__name__}: {str(e)}")
