import os
import django
from dotenv import load_dotenv

# Load .env first
load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.db import connection

# SQL to create the missing tables
sql_scripts = [
    # Create Slide table
    """
    CREATE TABLE IF NOT EXISTS `core_slide` (
        `id` int AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `caption1` varchar(100) NOT NULL,
        `caption2` varchar(100) NOT NULL,
        `link` varchar(100) NOT NULL,
        `image` varchar(100) NOT NULL,
        `is_active` bool NOT NULL DEFAULT true
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """,
    
    # Create Category table
    """
    CREATE TABLE IF NOT EXISTS `core_category` (
        `id` int AUTO_INCREMENT NOT NULL PRIMARY KEY,
        `title` varchar(100) NOT NULL,
        `slug` varchar(50) NOT NULL,
        `description` longtext NOT NULL,
        `image` varchar(100) NOT NULL,
        `is_active` bool NOT NULL DEFAULT true,
        UNIQUE KEY `slug` (`slug`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
    """
]

with connection.cursor() as cursor:
    for sql in sql_scripts:
        try:
            cursor.execute(sql)
            print(f"✓ Executed: {sql[:50]}...")
        except Exception as e:
            print(f"✗ Error: {e}")
            
print("\nTables created successfully!")

# Verify
with connection.cursor() as cursor:
    cursor.execute("SHOW TABLES LIKE 'core_%'")
    tables = [row[0] for row in cursor.fetchall()]
    print(f"\nCurrent core tables: {sorted(tables)}")
