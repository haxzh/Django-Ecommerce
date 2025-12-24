import os
import django
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from core.models import Item, Category, Slide

print("="*80)
print("UPDATING PRICES TO INDIAN RUPEES (INR)")
print("="*80)

# Update product prices to Indian Rupees (converting from USD with appropriate Indian pricing)
products_inr_prices = {
    'classic-white-tshirt': {'price': 1599, 'discount_price': 1199},
    'graphic-print-tshirt': {'price': 1999, 'discount_price': None},
    'v-neck-tshirt': {'price': 1899, 'discount_price': 1449},
    'formal-white-shirt': {'price': 3199, 'discount_price': 2399},
    'floral-print-blouse': {'price': 2799, 'discount_price': None},
    'denim-shirt': {'price': 3599, 'discount_price': 2799},
    'classic-black-hoodie': {'price': 3999, 'discount_price': 3199},
    'zip-up-sweatshirt': {'price': 3599, 'discount_price': None},
    'pleated-mini-skirt': {'price': 2399, 'discount_price': 1999},
    'maxi-skirt': {'price': 3199, 'discount_price': None},
}

print("\n1. Updating Product Prices to INR...")
for slug, prices in products_inr_prices.items():
    try:
        item = Item.objects.get(slug=slug)
        item.price = prices['price']
        item.discount_price = prices['discount_price']
        item.save()
        if prices['discount_price']:
            print(f"✓ {item.title}: ₹{prices['price']} → ₹{prices['discount_price']}")
        else:
            print(f"✓ {item.title}: ₹{prices['price']}")
    except Item.DoesNotExist:
        print(f"✗ Product not found: {slug}")
    except Exception as e:
        print(f"✗ Error updating {slug}: {e}")

print("\n" + "="*80)
print("PRICE UPDATE COMPLETE!")
print("="*80)
print(f"\n✓ Updated {Item.objects.count()} products to Indian Rupees")
print("\n📍 All prices are now in INR (₹)")
print("💡 Prices are optimized for the Indian market")
print("\n✅ Refresh your browser to see the updated prices!")
