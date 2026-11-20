# ======================================================
# Module 03 Assignment : Payment-wise Sales Analysis
# Course : Ostad Data Engineering Bootcamp
# File : payment_tools.py


import os
PATH = os.path.join("module-02", "data", "raw_sales.txt")

with open(PATH, encoding='utf-8') as fh:
    lines = fh.read().strip().split('\n')
print("Total records:", len(lines))

# payment_method wise calculation
bkash_total = 0.0
bkash_count = 0

nagad_total = 0.0
nagad_count = 0

card_total = 0.0
card_count = 0

rocket_total = 0.0
rocket_count = 0

cash_total = 0.0
cash_count = 0

for raw in lines:
    parts   = raw.split(";")
    amount  = float(parts[5].strip().replace("৳", "").replace(",", ""))
    payment = parts[6].strip().lower()
    status  = parts[7].strip().lower()
    
    if status == 'cancelled':
        continue
    elif payment == 'bkash':
        bkash_total += amount
        bkash_count += 1
    
    elif payment == 'nagad':
            nagad_total += amount
            nagad_count += 1
    
    elif payment == 'rocket':
            rocket_total += amount
            rocket_count += 1
    
    elif payment == 'card':
            card_total += amount
            card_count += 1
            
    else:
            cash_total += amount
            cash_count += 1
            

print("payment ধরে হিসাব (বাতিল বাদে)\n")

print(f"bkash             {bkash_count}টা   ৳{bkash_total:.2f}")
print(f"nagad             {nagad_count}টা   ৳{nagad_total:.2f}")
print(f"card              {card_count}টা   ৳{card_total:.2f}")
print(f"rocket            {rocket_count}টা   ৳{rocket_total:.2f}")
print(f"cash on delivery  {cash_count}টা   ৳{cash_total:.2f}")

total = bkash_total + nagad_total + card_total + rocket_total + cash_total

print(f"\nসব মিলিয়ে: ৳{total:.2f}")

