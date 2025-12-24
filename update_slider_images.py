import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')
django.setup()

from core.models import Slide

def update_slider_images():
    """Update slider images to use actual image files"""
    
    # Define slider image mappings
    slider_updates = [
        {
            'caption1': 'New Collection',
            'caption2': 'Shop Latest Fashion Trends',
            'image': 'add_slide_1.jpg',
        },
        {
            'caption1': 'Summer Sale',
            'caption2': 'UP TO 50% OFF ON SELECTED ITEMS',
            'image': '1920x678-1.jpg',
        },
        {
            'caption1': 'Premium Quality',
            'caption2': 'Best Prices Guaranteed',
            'image': 'kr_slide_add_2.jpg',
        },
    ]
    
    print("\n" + "="*50)
    print("UPDATING SLIDER IMAGES")
    print("="*50)
    
    # First, delete all existing sliders
    existing_count = Slide.objects.count()
    Slide.objects.all().delete()
    print(f"\n✓ Deleted {existing_count} existing sliders")
    
    # Create new sliders with proper images
    for slider_data in slider_updates:
        try:
            slide = Slide.objects.create(
                caption1=slider_data['caption1'],
                caption2=slider_data['caption2'],
                link='/shop/',
                image=slider_data['image'],
                is_active=True
            )
            print(f"✓ Created slider: {slide.caption1} - Image: {slide.image}")
        except Exception as e:
            print(f"✗ Error creating slider '{slider_data['caption1']}': {e}")
    
    print("\n" + "="*50)
    print("SLIDER UPDATE COMPLETE")
    print("="*50)
    print(f"\nTotal sliders: {Slide.objects.count()}")
    
    # Display all sliders
    print("\nCurrent Sliders:")
    for slide in Slide.objects.all():
        print(f"  - {slide.caption1}: {slide.image}")

if __name__ == "__main__":
    update_slider_images()
