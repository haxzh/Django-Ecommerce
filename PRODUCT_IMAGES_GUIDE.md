# Product Images Setup Guide

## ✅ Current Status
All products, categories, and sliders now have images assigned from your `media_root` folder.

## 📸 Current Image Assignments

### Products:
- **Classic White T-Shirt** → add.webp
- **Graphic Print T-Shirt** → add2.jpg  
- **V-Neck T-Shirt** → add3.webp
- **Formal White Shirt** → add4.webp
- **Floral Print Blouse** → add5.webp
- **Denim Shirt** → add6.jpg
- **Classic Black Hoodie** → add7.webp
- **Zip-Up Sweatshirt** → add8.webp
- **Pleated Mini Skirt** → add9.webp
- **Maxi Skirt** → add10.webp

### Categories:
- **Shirts And Blouses** → banner-02.webp
- **T-Shirts** → banner-03.webp
- **Skirts** → banner-04.webp
- **Hoodies & Sweatshirts** → banner-07.webp

### Sliders:
- **New Collection** → add_slide_1.jpg
- **Summer Sale** → 1920x678-1.jpg
- **Premium Quality** → kr_slide_add_2.jpg

## 🔄 To Update Images

### Option 1: Via Django Admin
1. Go to http://127.0.0.1:8000/admin/
2. Login with `admin` / `admin123`
3. Click on "Items" or "Categories" or "Slides"
4. Click on any product/category/slide
5. Upload a new image in the "Image" field
6. Click "Save"

### Option 2: Add New Images to media_root
1. Add your new product images to `media_root/` folder
2. Update the image filenames in the admin panel

### Option 3: Run Update Script Again
If you add more images to `media_root/`, you can modify and run `update_product_images.py` again.

## 📝 Adding More Products

To add more products with images:

```python
# In Django Admin or via script:
from core.models import Item, Category

category = Category.objects.get(slug='t-shirts')
Item.objects.create(
    title='New Product Name',
    price=29.99,
    discount_price=24.99,
    category=category,
    label='N',  # 'N' for New, 'S' for Sale, 'P' for Promotion
    slug='new-product-slug',
    stock_no='TS999',
    description_short='Short description',
    description_long='Long detailed description',
    image='add11.webp',  # Your image filename
    is_active=True
)
```

## 🖼️ Image Requirements

- **Product Images**: Recommended size 600x600px or larger (square)
- **Category Banners**: Recommended size 600x400px
- **Slider Images**: Recommended size 1920x570px (widescreen)
- **Formats**: JPG, PNG, WebP

## 💡 Tips

1. Use descriptive filenames for images (e.g., `red-tshirt-front.jpg`)
2. Optimize images before uploading to reduce file size
3. Keep consistent aspect ratios for product images
4. Test images on mobile devices for responsiveness

## 🚀 Next Steps

1. Refresh your browser to see all product images
2. Customize product details in Django Admin
3. Upload your own product photos
4. Adjust prices and descriptions as needed
