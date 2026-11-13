
# ============================================================
# Assignment 04: Variables, Data Types & String Manipulation
# Course: Ostad Data Engineering Bootcamp
# Module: 02 | Class: 04
# File: clean_three.py
#
# Objective:
# Clean and standardize three raw sales records using
# Python string methods, type conversion, and f-strings.
#
# Concepts Practiced:
# - Variables and Data Types
# - String Methods (split, strip, upper, lower, title)
# - Type Conversion (int, float)
# - Arithmetic Operations
# - Formatted Strings (f-strings)
# ============================================================


# 1. Raw Sales Records

raw_a = "  ord100047 ;2026-10-08;  Tanvir Hossain  ; Dim 12pc ;3; ৳ 441.75 ; Cash on Delivery ;DELIVERED"

raw_b = "ORD100048 ; 2026-10-08 ; SUMAIYA  KHAN ; Ilish 1kg ;1;৳ 1,520.00; bkash ; cancelled"

raw_c = "ord100049;2026-10-09; rakib  mia ;Broiler Murgi 1kg; 4 ;৳ 812.00;Card;delivered"


# 2. Clean Record A

# Strip in 8 parts 
parts_a = raw_a.split(";")

order_id_a = parts_a[0]
order_date_a = parts_a[1]
customer_name_a = parts_a[2]
product_a = parts_a[3]
quantity_a = parts_a[4]
amount_text_a = parts_a[5]
payment_a = parts_a[6]
status_a = parts_a[7]

# Remove empty space 
order_id_a = order_id_a.strip()
order_date_a = order_date_a.strip()
customer_name_a = " ".join(customer_name_a.split())
product_a = product_a.strip()
quantity_a = quantity_a.strip()
amount_text_a = amount_text_a.strip()
payment_a = payment_a.strip()
status_a = status_a.strip()

# Fix letter case
order_id_a = order_id_a.upper()
customer_name_a = customer_name_a.title()
payment_a = payment_a.lower()
status_a = status_a.lower()

# Type conversion
quantity_a = int(quantity_a)
amount_text_a = amount_text_a.replace("৳", "").replace(",", "").strip()
total_amount_a = float(amount_text_a)

# Unit price calculation
unit_price_a = total_amount_a / quantity_a

# Summary print 
print(f"{order_id_a}  ·  {order_date_a}")
print(f"{customer_name_a} কিনেছেন {product_a} — {quantity_a}টা")
print(f"মোট ৳{total_amount_a:.2f}  (প্রতিটা ৳{unit_price_a:.2f})")
print(f"পেমেন্ট: {payment_a}  ·  অবস্থা: {status_a}")


# 3. Clean Record B

# Split into 8 parts
parts_b = raw_b.split(";")

order_id_b = parts_b[0]
order_date_b = parts_b[1]
customer_name_b = parts_b[2]
product_b = parts_b[3]
quantity_b = parts_b[4]
amount_text_b = parts_b[5]
payment_b = parts_b[6]
status_b = parts_b[7]

# Remove empty spaces
order_id_b = order_id_b.strip()
order_date_b = order_date_b.strip()
customer_name_b = " ".join(customer_name_b.split())
product_b = product_b.strip()
quantity_b = quantity_b.strip()
amount_text_b = amount_text_b.strip()
payment_b = payment_b.strip()
status_b = status_b.strip()

# Fix letter case
order_id_b = order_id_b.upper()
customer_name_b = customer_name_b.title()
payment_b = payment_b.lower()
status_b = status_b.lower()

# Type conversion
quantity_b = int(quantity_b)
amount_text_b = amount_text_b.replace("৳", "").replace(",", "").strip()
total_amount_b = float(amount_text_b)

# Unit price calculation
unit_price_b = total_amount_b / quantity_b

# Cancellation warning (Bonus)
print()
print("সতর্কতা: এই অর্ডারটা বাতিল হয়েছে, হিসাবে ধরবেন না।")

# Summary print
print(f"{order_id_b}  ·  {order_date_b}")
print(f"{customer_name_b} কিনেছেন {product_b} — {quantity_b}টা")
print(f"মোট ৳{total_amount_b:.2f}  (প্রতিটা ৳{unit_price_b:.2f})")
print(f"পেমেন্ট: {payment_b}  ·  অবস্থা: {status_b}")



# 4. Clean Record C

# Split into 8 parts
parts_c = raw_c.split(";")

order_id_c = parts_c[0]
order_date_c = parts_c[1]
customer_name_c = parts_c[2]
product_c = parts_c[3]
quantity_c = parts_c[4]
amount_text_c = parts_c[5]
payment_c = parts_c[6]
status_c = parts_c[7]

# Remove empty spaces
order_id_c = order_id_c.strip()
order_date_c = order_date_c.strip()
customer_name_c = " ".join(customer_name_c.split())
product_c = product_c.strip()
quantity_c = quantity_c.strip()
amount_text_c = amount_text_c.strip()
payment_c = payment_c.strip()
status_c = status_c.strip()

# Fix letter case
order_id_c = order_id_c.upper()
customer_name_c = customer_name_c.title()
payment_c = payment_c.lower()
status_c = status_c.lower()

# Type conversion
quantity_c = int(quantity_c)
amount_text_c = amount_text_c.replace("৳", "").replace(",", "").strip()
total_amount_c = float(amount_text_c)

# Unit price calculation
unit_price_c = total_amount_c / quantity_c

# Summary print
print()
print(f"{order_id_c}  ·  {order_date_c}")
print(f"{customer_name_c} কিনেছেন {product_c} — {quantity_c}টা")
print(f"মোট ৳{total_amount_c:.2f}  (প্রতিটা ৳{unit_price_c:.2f})")
print(f"পেমেন্ট: {payment_c}  ·  অবস্থা: {status_c}")