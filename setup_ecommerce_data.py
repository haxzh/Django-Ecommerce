import os
import django
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from django.contrib.auth import get_user_model
from core.models import Category, Item, Slide

User = get_user_model()

print("="*80)
print("SETTING UP COMPLETE ECOMMERCE DATA")
print("="*80)

# 1. Create superuser if doesn't exist
print("\n1. Creating Admin User...")
try:
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@ecommerce.com',
            password='admin123'
        )
        print("✓ Admin user created: username='admin', password='admin123'")
    else:
        admin = User.objects.get(username='admin')
        admin.set_password('admin123')
        admin.save()
        print("✓ Admin user already exists. Password reset to 'admin123'")
except Exception as e:
    print(f"✗ Error creating admin: {e}")

# 2. Create Categories
print("\n2. Creating Categories...")
categories_data = [
    {
        'title': 'Shirts And Blouses',
        'slug': 'shirts-blouses',
        'description': 'Stylish shirts and blouses for every occasion',
    },
    {
        'title': 'T-Shirts',
        'slug': 't-shirts',
        'description': 'Comfortable and trendy t-shirts',
    },
    {
        'title': 'Skirts',
        'slug': 'skirts',
        'description': 'Elegant skirts for women',
    },
    {
        'title': 'Hoodies & Sweatshirts',
        'slug': 'hoodies-sweatshirts',
        'description': 'Cozy hoodies and sweatshirts',
    },
]

for cat_data in categories_data:
    try:
        category, created = Category.objects.get_or_create(
            slug=cat_data['slug'],
            defaults={
                'title': cat_data['title'],
                'description': cat_data['description'],
                'image': 'banner-02.webp',
                'is_active': True
            }
        )
        if created:
            print(f"✓ Created category: {category.title}")
        else:
            print(f"✓ Category exists: {category.title}")
    except Exception as e:
        print(f"✗ Error creating category {cat_data['title']}: {e}")

# 3. Create Sample Products
print("\n3. Creating Sample Products...")
categories = Category.objects.all()

if categories.exists():
    products_data = [
        # T-Shirts
        {
            'title': 'Classic White T-Shirt',
            'price': 19.99,
            'discount_price': 14.99,
            'category_slug': 't-shirts',
            'label': 'S',
            'slug': 'classic-white-tshirt',
            'stock_no': 'TS001',
            'description_short': 'Premium quality white t-shirt',
            'description_long': 'Made from 100% cotton, this classic white t-shirt is perfect for everyday wear. Comfortable fit and durable material.',
            'image': 'add.webp',
        },
        {
            'title': 'Graphic Print T-Shirt',
            'price': 24.99,
            'discount_price': None,
            'category_slug': 't-shirts',
            'label': 'N',
            'slug': 'graphic-print-tshirt',
            'stock_no': 'TS002',
            'description_short': 'Trendy graphic design t-shirt',
            'description_long': 'Express yourself with this stylish graphic print t-shirt. Available in multiple colors.',
            'image': 'add2.jpg',
        },
        {
            'title': 'V-Neck T-Shirt',
            'price': 22.99,
            'discount_price': 17.99,
            'category_slug': 't-shirts',
            'label': 'P',
            'slug': 'v-neck-tshirt',
            'stock_no': 'TS003',
            'description_short': 'Elegant V-neck design',
            'description_long': 'Sophisticated V-neck t-shirt perfect for casual and semi-formal occasions.',
            'image': 'add3.webp',
        },
        
        # Shirts & Blouses
        {
            'title': 'Formal White Shirt',
            'price': 39.99,
            'discount_price': 29.99,
            'category_slug': 'shirts-blouses',
            'label': 'S',
            'slug': 'formal-white-shirt',
            'stock_no': 'SH001',
            'description_short': 'Professional white formal shirt',
            'description_long': 'Perfect for office wear, this formal white shirt features a classic cut and premium fabric.',
            'image': 'add4.webp',
        },
        {
            'title': 'Floral Print Blouse',
            'price': 34.99,
            'discount_price': None,
            'category_slug': 'shirts-blouses',
            'label': 'N',
            'slug': 'floral-print-blouse',
            'stock_no': 'BL001',
            'description_short': 'Beautiful floral pattern blouse',
            'description_long': 'Elegant floral print blouse with a comfortable fit, perfect for spring and summer.',
            'image': 'add5.webp',
        },
        {
            'title': 'Denim Shirt',
            'price': 44.99,
            'discount_price': 34.99,
            'category_slug': 'shirts-blouses',
            'label': 'P',
            'slug': 'denim-shirt',
            'stock_no': 'SH002',
            'description_short': 'Stylish denim shirt',
            'description_long': 'Versatile denim shirt that pairs well with jeans or skirts. Durable and fashionable.',
            'image': 'add6.jpg',
        },
        
        # Hoodies & Sweatshirts
        {
            'title': 'Classic Black Hoodie',
            'price': 49.99,
            'discount_price': 39.99,
            'category_slug': 'hoodies-sweatshirts',
            'label': 'S',
            'slug': 'classic-black-hoodie',
            'stock_no': 'HD001',
            'description_short': 'Warm and comfortable black hoodie',
            'description_long': 'Premium quality hoodie with soft fleece lining. Perfect for cold weather.',
            'image': 'add7.webp',
        },
        {
            'title': 'Zip-Up Sweatshirt',
            'price': 44.99,
            'discount_price': None,
            'category_slug': 'hoodies-sweatshirts',
            'label': 'N',
            'slug': 'zip-up-sweatshirt',
            'stock_no': 'SW001',
            'description_short': 'Convenient zip-up design',
            'description_long': 'Easy to wear zip-up sweatshirt with side pockets. Great for outdoor activities.',
            'image': 'add8.webp',
        },
        
        # Skirts
        {
            'title': 'Pleated Mini Skirt',
            'price': 29.99,
            'discount_price': 24.99,
            'category_slug': 'skirts',
            'label': 'S',
            'slug': 'pleated-mini-skirt',
            'stock_no': 'SK001',
            'description_short': 'Elegant pleated design',
            'description_long': 'Classic pleated mini skirt that goes with any top. Perfect for casual outings.',
            'image': 'add9.webp',
        },
        {
            'title': 'Maxi Skirt',
            'price': 39.99,
            'discount_price': None,
            'category_slug': 'skirts',
            'label': 'N',
            'slug': 'maxi-skirt',
            'stock_no': 'SK002',
            'description_short': 'Flowing maxi length skirt',
            'description_long': 'Elegant maxi skirt with a flowing design. Perfect for summer days and evening events.',
            'image': 'add10.webp',
        },
    ]
    
    for product_data in products_data:
        try:
            category = Category.objects.get(slug=product_data['category_slug'])
            item, created = Item.objects.get_or_create(
                slug=product_data['slug'],
                defaults={
                    'title': product_data['title'],
                    'price': product_data['price'],
                    'discount_price': product_data['discount_price'],
                    'category': category,
                    'label': product_data['label'],
                    'stock_no': product_data['stock_no'],
                    'description_short': product_data['description_short'],
                    'description_long': product_data['description_long'],
                    'image': product_data.get('image', 'item-10.webp'),
                    'is_active': True
                }
            )
            if created:
                print(f"✓ Created product: {item.title} (${item.price})")
            else:
                print(f"✓ Product exists: {item.title}")
        except Exception as e:
            print(f"✗ Error creating product {product_data['title']}: {e}")
else:
    print("✗ No categories found. Cannot create products.")

# 4. Create Slider/Banner Images
print("\n4. Creating Homepage Sliders...")
sliders_data = [
    {
        'caption1': 'New Collection',
        'caption2': 'Shop Latest Fashion Trends',
        'link': '/shop/',
        'image': 'add_slide_1.jpg',
    },
    {
        'caption1': 'Summer Sale',
        'caption2': 'Up to 50% Off on Selected Items',
        'link': '/shop/',
        'image': '1920x678-1.jpg',
    },
    {
        'caption1': 'Premium Quality',
        'caption2': 'Best Prices Guaranteed',
        'link': '/shop/',
        'image': 'kr_slide_add_2.jpg',
    },
]

for slider_data in sliders_data:
    try:
        slide, created = Slide.objects.get_or_create(
            caption1=slider_data['caption1'],
            defaults={
                'caption2': slider_data['caption2'],
                'link': slider_data['link'],
                'image': slider_data.get('image', 'light-bulbs--1920x570.jpg'),
                'is_active': True
            }
        )
        if created:
            print(f"✓ Created slider: {slide.caption1}")
        else:
            print(f"✓ Slider exists: {slide.caption1}")
    except Exception as e:
        print(f"✗ Error creating slider: {e}")

# 5. Summary
print("\n" + "="*80)
print("SETUP COMPLETE!")
print("="*80)
print("\nDatabase Summary:")
print(f"✓ Categories: {Category.objects.count()}")
print(f"✓ Products: {Item.objects.count()}")
print(f"✓ Sliders: {Slide.objects.count()}")
print(f"✓ Users: {User.objects.count()}")

print("\n" + "="*80)
print("ADMIN LOGIN CREDENTIALS:")
print("="*80)
print("URL:      http://127.0.0.1:8000/admin/")
print("Username: admin")
print("Password: admin123")
print("="*80)

print("\nWebsite URLs:")
print("  Homepage:  http://127.0.0.1:8000/")
print("  Shop:      http://127.0.0.1:8000/shop/")
print("  Admin:     http://127.0.0.1:8000/admin/")

print("\n✅ Your ecommerce website is now FULLY FUNCTIONAL!")
print("✅ You can now login to admin and manage products")
print("✅ Customers can browse and buy products")
