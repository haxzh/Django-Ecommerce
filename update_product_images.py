import os
import django
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from core.models import Item, Category, Slide

print("="*80)
print("UPDATING PRODUCT AND CATEGORY IMAGES")
print("="*80)

# Update product images
products_images = {
    'classic-white-tshirt': 'add.webp',
    'graphic-print-tshirt': 'add2.jpg',
    'v-neck-tshirt': 'add3.webp',
    'formal-white-shirt': 'add4.webp',
    'floral-print-blouse': 'add5.webp',
    'denim-shirt': 'add6.jpg',
    'classic-black-hoodie': 'add7.webp',
    'zip-up-sweatshirt': 'add8.webp',
    'pleated-mini-skirt': 'add9.webp',
    'maxi-skirt': 'add10.webp',
}

print("\n1. Updating Product Images...")
for slug, image_name in products_images.items():
    try:
        item = Item.objects.get(slug=slug)
        item.image = image_name
        item.save()
        print(f"✓ Updated image for: {item.title} -> {image_name}")
    except Item.DoesNotExist:
        print(f"✗ Product not found: {slug}")
    except Exception as e:
        print(f"✗ Error updating {slug}: {e}")

# Update category images
print("\n2. Updating Category Images...")
categories = Category.objects.all()
category_images = [
    'banner-02.webp',
    'banner-03.webp', 
    'banner-04.webp',
    'banner-07.webp'
]

for idx, category in enumerate(categories):
    try:
        image_name = category_images[idx % len(category_images)]
        category.image = image_name
        category.save()
        print(f"✓ Updated image for category: {category.title} -> {image_name}")
    except Exception as e:
        print(f"✗ Error updating category {category.title}: {e}")

# Update slider images
print("\n3. Updating Slider Images...")
slider_images = {
    'New Collection': 'add_slide_1.jpg',
    'Summer Sale': '1920x678-1.jpg',
    'Premium Quality': 'kr_slide_add_2.jpg',
}

for caption, image_name in slider_images.items():
    try:
        slide = Slide.objects.get(caption1=caption)
        slide.image = image_name
        slide.save()
        print(f"✓ Updated slider image: {caption} -> {image_name}")
    except Slide.DoesNotExist:
        print(f"✗ Slider not found: {caption}")
    except Exception as e:
        print(f"✗ Error updating slider {caption}: {e}")

print("\n" + "="*80)
print("UPDATE COMPLETE!")
print("="*80)
print(f"\n✓ Updated {Item.objects.count()} products")
print(f"✓ Updated {Category.objects.count()} categories")
print(f"✓ Updated {Slide.objects.count()} sliders")
print("\n✅ All images have been updated! Refresh your browser to see the changes.")
