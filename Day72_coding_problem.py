# ✅ Day 72: E-commerce Cart API with Coupon Logic
# --------------------------------------------------------------
# 👉 Task: Develop an API to manage an e-commerce cart with discount and coupon functionality.



# 🔥 API Endpoints:
# - POST /cart/ → Add item to cart
# - GET /cart/ → View cart items
# - POST /apply-coupon/ → Apply a coupon
# - GET /checkout/ → Calculate final price

# 🎉 Expected Input (Add Item):
"""
{
  "product_id": 1,
  "quantity": 2
}
"""

# 🎉 Expected Output:
"""
{
  "cart_total": 1000,
  "items": [
    {"product_id": 1, "name": "Smartphone", "quantity": 2, "price": 500}
  ]
}
"""

# 🎉 Apply Coupon:
"""
{
  "coupon_code": "DISCOUNT10"
}
"""


# -----------------------------------------------------------------