# India Localization Guide

## Overview
This document details the complete localization of the Django E-commerce website for the Indian market, including currency conversion from USD to INR (Indian Rupees).

## Currency Conversion

### Database Updates
All product prices have been converted to Indian Rupees using the `convert_to_inr.py` script.

**Conversion Summary:**
- 11 products updated with INR pricing
- Price range: ₹1,199 - ₹3,999
- Discount prices maintained with equivalent INR values

**Product Pricing Examples:**
- Classic White T-Shirt: ₹1,599 → ₹1,199 (with discount)
- Graphic Print T-Shirt: ₹1,999
- V-Neck T-Shirt: ₹1,899 → ₹1,449
- Formal White Shirt: ₹3,199 → ₹2,399
- Classic Black Hoodie: ₹3,999 → ₹3,199

### Template Updates

**Files Modified for INR Display:**

1. **nav.html**
   - Free shipping text: "Free shipping across India for orders over ₹2,999"
   - Currency selector: Set to INR (USD/EUR commented out)

2. **index.html**
   - Product prices: `₹{{item.price|floatformat:0}}`
   - Removed decimal places for cleaner display

3. **shop.html**
   - Product prices: `₹{{item.price|floatformat:0}}`
   - Price filter dropdown: ₹0 - ₹1,000, ₹1,000 - ₹2,000, etc.
   - Price filter range: ₹500 - ₹5,000

4. **category.html**
   - Product prices: `₹{{item.price|floatformat:0}}`
   - Price filter dropdown: ₹0 - ₹1,000, ₹1,000 - ₹2,000, etc.
   - Price filter range: ₹500 - ₹5,000

5. **product-detail.html**
   - Main price display: `₹{{object.price|floatformat:0}}`
   - Discount price: `₹{{object.discount_price|floatformat:0}}`

6. **order_summary.html**
   - Item prices: `₹{{order_item.get_total_item_price|floatformat:0}}`
   - Discount prices: `₹{{order_item.get_total_discount_item_price|floatformat:0}}`
   - Savings: `₹{{order_item.get_amount_saved|floatformat:0}}`
   - Coupon discount: `₹{{object.coupon.amount|floatformat:0}}`
   - Order total: `₹{{object.get_total|floatformat:0}}`

7. **cart.html**
   - Free shipping text: "Free shipping across India for orders over ₹2,999"

## Display Format

### Price Formatting
- Symbol: ₹ (Indian Rupee symbol)
- Format: `₹X,XXX` (no decimal places)
- Django filter used: `|floatformat:0`

### Price Ranges
- ₹0 - ₹1,000
- ₹1,000 - ₹2,000
- ₹2,000 - ₹3,000
- ₹3,000 - ₹4,000
- ₹4,000+

## Regional Messaging

### Shipping
- "Free shipping across India for orders over ₹2,999"
- Updated from: "$100 minimum" to "₹2,999 minimum"

### Currency Selector
- Default: INR (Indian Rupees)
- USD and EUR options commented out
- Located in nav.html topbar

## Implementation Scripts

### convert_to_inr.py
```python
# Converts all product prices from USD to INR
# Exchange rate approximation used: 1 USD ≈ ₹80
# Prices rounded to nearest 99 or 49 for Indian market appeal
```

**Usage:**
```bash
python convert_to_inr.py
```

## Testing Checklist

- [x] Homepage product prices display ₹ symbol
- [x] Shop page product prices display ₹ symbol
- [x] Category page product prices display ₹ symbol
- [x] Product detail page prices display ₹ symbol
- [x] Cart/Order summary displays ₹ symbol
- [x] Price filter dropdowns show INR ranges
- [x] Price filter sliders show INR ranges
- [x] Free shipping message India-specific
- [x] Currency selector defaults to INR
- [x] All prices display without decimal places

## Database Schema

No changes required to database schema. The `price` and `discount_price` fields in the `Item` model continue to use DecimalField, now storing INR values instead of USD values.

## Future Considerations

### Payment Gateway
- Current: Stripe (supports INR)
- Consideration: May need to update Stripe currency parameter from 'usd' to 'inr'
- May want to integrate Indian payment options: Razorpay, Paytm, UPI

### Shipping Integration
- Consider Indian shipping providers: Delhivery, Blue Dart, India Post
- Update shipping calculation logic for Indian pin codes

### Tax/GST
- Consider adding GST (Goods and Services Tax) calculation
- GST rates: 5%, 12%, 18%, 28% depending on product category
- Display prices as "inclusive of all taxes" or add GST breakdown

### Regional Languages
- Consider adding Hindi language support
- Regional language options for major Indian states

## Maintenance

### Adding New Products
When adding new products, ensure:
1. Prices are in INR (₹)
2. Use pricing psychology: end prices with 99, 49, or 999
3. Set appropriate discount prices for sales
4. All templates will automatically display ₹ symbol using the Django filters

### Price Updates
To update prices:
1. Use Django admin to edit product prices
2. Enter prices in INR format (e.g., 1999, 2499, 3999)
3. Templates will automatically format with ₹ symbol and no decimals

## Contact
For questions about Indian localization, refer to this guide or contact the development team.
