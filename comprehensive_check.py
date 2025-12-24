import os
import sys
import django
from dotenv import load_dotenv

# Load environment
load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.core.management import call_command
from django.db import connection
from django.apps import apps
import importlib.util

print("="*80)
print("COMPREHENSIVE PROJECT CHECK")
print("="*80)

# 1. Check Python syntax in all .py files
print("\n1. CHECKING PYTHON SYNTAX...")
print("-"*80)
error_count = 0
checked_files = 0

for root, dirs, files in os.walk('.'):
    # Skip virtual environment and cache
    if 'env' in root or '__pycache__' in root or '.git' in root:
        continue
    
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(root, file)
            checked_files += 1
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    compile(f.read(), filepath, 'exec')
            except SyntaxError as e:
                print(f"  ✗ SYNTAX ERROR in {filepath}: {e}")
                error_count += 1

if error_count == 0:
    print(f"  ✓ All {checked_files} Python files have valid syntax")
else:
    print(f"  ✗ Found {error_count} syntax errors in {checked_files} files")

# 2. Check database tables
print("\n2. CHECKING DATABASE TABLES...")
print("-"*80)
try:
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        print(f"  ✓ Found {len(tables)} tables in database")
        
        # Check core app tables
        core_tables = [t for t in tables if t.startswith('core_')]
        print(f"  ✓ Core app tables: {', '.join(core_tables)}")
        
        # Verify table structures
        missing_tables = []
        for model in apps.get_app_config('core').get_models():
            table_name = model._meta.db_table
            if table_name not in tables:
                missing_tables.append(table_name)
                print(f"  ✗ Missing table: {table_name}")
        
        if not missing_tables:
            print(f"  ✓ All core model tables exist")
            
except Exception as e:
    print(f"  ✗ Database error: {e}")

# 3. Check migrations
print("\n3. CHECKING MIGRATIONS...")
print("-"*80)
try:
    from django.db.migrations.loader import MigrationLoader
    loader = MigrationLoader(connection)
    
    # Check for unapplied migrations
    graph = loader.graph
    targets = graph.leaf_nodes()
    plan = []
    seen = set()
    
    for target in targets:
        for migration in graph.forwards_plan(target):
            if migration not in seen:
                seen.add(migration)
                plan.append(migration)
    
    applied = loader.applied_migrations
    unapplied = [m for m in plan if m not in applied]
    
    if unapplied:
        print(f"  ⚠ {len(unapplied)} unapplied migrations:")
        for migration in unapplied[:5]:  # Show first 5
            print(f"    - {migration[0]}.{migration[1]}")
    else:
        print(f"  ✓ All migrations applied")
        
except Exception as e:
    print(f"  ✗ Migration check error: {e}")

# 4. Check required files
print("\n4. CHECKING REQUIRED FILES...")
print("-"*80)
required_files = [
    'manage.py',
    'requirements.txt',
    '.env',
    'demo/settings.py',
    'demo/urls.py',
    'demo/wsgi.py',
    'core/models.py',
    'core/views.py',
    'core/urls.py',
    'templates/base.html',
]

for file in required_files:
    if os.path.exists(file):
        print(f"  ✓ {file}")
    else:
        print(f"  ✗ MISSING: {file}")

# 5. Check template syntax
print("\n5. CHECKING TEMPLATES...")
print("-"*80)
template_errors = 0
template_count = 0

if os.path.exists('templates'):
    for root, dirs, files in os.walk('templates'):
        for file in files:
            if file.endswith('.html'):
                template_count += 1
                filepath = os.path.join(root, file)
                try:
                    from django.template import engines
                    django_engine = engines['django']
                    django_engine.get_template(filepath.replace('templates/', ''))
                except Exception as e:
                    print(f"  ✗ Template error in {filepath}: {str(e)[:100]}")
                    template_errors += 1

if template_errors == 0:
    print(f"  ✓ All {template_count} templates are valid")
else:
    print(f"  ⚠ Found {template_errors} template warnings in {template_count} templates")

# 6. Check static files
print("\n6. CHECKING STATIC FILES...")
print("-"*80)
if os.path.exists('static_in_env'):
    print(f"  ✓ static_in_env directory exists")
    css_files = len([f for f in os.listdir('static_in_env/css') if f.endswith('.css')])
    js_files = len([f for f in os.listdir('static_in_env/js') if f.endswith('.js')])
    print(f"  ✓ Found {css_files} CSS files and {js_files} JS files")
else:
    print(f"  ✗ static_in_env directory missing")

# 7. Check environment variables
print("\n7. CHECKING ENVIRONMENT VARIABLES...")
print("-"*80)
required_env_vars = [
    'SECRET_KEY',
    'DEBUG',
    'MYSQL_DATABASE',
    'MYSQL_USER',
    'MYSQL_PASSWORD',
    'MYSQL_HOST',
]

for var in required_env_vars:
    if os.getenv(var):
        # Don't print sensitive values
        if var in ['SECRET_KEY', 'MYSQL_PASSWORD']:
            print(f"  ✓ {var} is set (hidden)")
        else:
            print(f"  ✓ {var} = {os.getenv(var)}")
    else:
        print(f"  ✗ MISSING: {var}")

# 8. Check installed packages
print("\n8. CHECKING DEPENDENCIES...")
print("-"*80)
try:
    with open('requirements.txt', 'r') as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    
    missing_packages = []
    for req in requirements[:10]:  # Check first 10
        package = req.split('==')[0].split('>=')[0].split('<=')[0]
        try:
            __import__(package.replace('-', '_'))
            print(f"  ✓ {package}")
        except ImportError:
            print(f"  ✗ MISSING: {package}")
            missing_packages.append(package)
    
    if len(requirements) > 10:
        print(f"  ... and {len(requirements)-10} more packages")
        
except Exception as e:
    print(f"  ⚠ Could not read requirements.txt: {e}")

# 9. Check model relationships
print("\n9. CHECKING MODEL RELATIONSHIPS...")
print("-"*80)
try:
    from core.models import Item, Category, Order, OrderItem
    
    # Try to query each model
    print(f"  ✓ Category model: {Category.objects.count()} records")
    print(f"  ✓ Item model: {Item.objects.count()} records")
    print(f"  ✓ Order model: {Order.objects.count()} records")
    print(f"  ✓ OrderItem model: {OrderItem.objects.count()} records")
    
except Exception as e:
    print(f"  ✗ Model relationship error: {e}")

# 10. Check URL patterns
print("\n10. CHECKING URL PATTERNS...")
print("-"*80)
try:
    from django.urls import get_resolver
    resolver = get_resolver()
    url_patterns = resolver.url_patterns
    print(f"  ✓ Found {len(url_patterns)} root URL patterns")
    
    # Check core URLs
    from core import urls as core_urls
    print(f"  ✓ Core app has {len(core_urls.urlpatterns)} URL patterns")
    
except Exception as e:
    print(f"  ✗ URL pattern error: {e}")

print("\n" + "="*80)
print("CHECK COMPLETE!")
print("="*80)
