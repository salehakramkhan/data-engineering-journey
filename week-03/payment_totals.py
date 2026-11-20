# ======================================================
# Module 03 Assignment : Payment-wise Sales Analysis
# Course : Ostad Data Engineering Bootcamp
# File : payment_totals.py


import os
import my_tools

PATH = os.path.join("module-02", "data", "raw_sales.txt")


# main function
def main():

    lines = my_tools.read_lines(PATH)

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

    # Bonus Task
    date_07_total = 0.0
    date_08_total = 0.0
    date_09_total = 0.0
    date_10_total = 0.0
    date_11_total = 0.0

    for raw in lines:

        parts = raw.split(";")
        amount = my_tools.clean_amount(parts[5])
        payment = parts[6].strip().lower()
        status = parts[7].strip().lower()
        date = parts[1].strip()

        if status == 'cancelled':
            continue

        # payment calculation
        if payment == 'bkash':
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

        # Bonus: date-wise calculation
        if date == '2026-10-07':
            date_07_total += amount

        elif date == '2026-10-08':
            date_08_total += amount

        elif date == '2026-10-09':
            date_09_total += amount

        elif date == '2026-10-10':
            date_10_total += amount

        elif date == '2026-10-11':
            date_11_total += amount

    # Payment-wise output
    print("payment ধরে হিসাব (বাতিল বাদে)\n")

    print(f"bkash             {bkash_count}টা   {my_tools.taka(bkash_total)}")
    print(f"nagad             {nagad_count}টা   {my_tools.taka(nagad_total)}")
    print(f"card              {card_count}টা   {my_tools.taka(card_total)}")
    print(f"rocket            {rocket_count}টা   {my_tools.taka(rocket_total)}")
    print(f"cash on delivery  {cash_count}টা   {my_tools.taka(cash_total)}")

    total = (bkash_total + nagad_total + card_total + rocket_total + cash_total)

    print(f"\nসব মিলিয়ে: {my_tools.taka(total)}")

    # Bonus: find highest sales date
    highest = max(
        date_07_total,
        date_08_total,
        date_09_total,
        date_10_total,
        date_11_total
    )

    if highest == date_07_total:
        highest_date = '2026-10-07'

    elif highest == date_08_total:
        highest_date = '2026-10-08'

    elif highest == date_09_total:
        highest_date = '2026-10-09'

    elif highest == date_10_total:
        highest_date = '2026-10-10'

    else:
        highest_date = '2026-10-11'

    print(f"\nসবচেয়ে বেশি টাকার অর্ডারের তারিখ: {highest_date}")


if __name__ == "__main__":
    main()