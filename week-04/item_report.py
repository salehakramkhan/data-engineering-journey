#!/usr/bin/env python3
import os
import sales_tools

PATH = os.path.join("module-04", "data", "raw_sales_week2.txt")


def parse_record(raw):
    parts = raw.split(";")
    return {
        "order_id": sales_tools.clean_id(parts[0]),
        "order_date": parts[1].strip(),
        "customer_name": sales_tools.clean_name(parts[2]),
        "item_name": parts[3].strip(),
        "quantity": int(parts[4].strip()),
        "amount": sales_tools.clean_amount(parts[5]),
        "payment": parts[6].strip().lower(),
        "status": parts[7].strip().lower(),
    }


def totals_by(records, key):
    totals = {}
    counts = {}
    for rec in records:
        name = rec[key]
        totals[name] = totals.get(name, 0.0) + rec["amount"]
        counts[name] = counts.get(name, 0) + 1
    return totals, counts


def level_1():
    with open(PATH, encoding="utf-8") as fh:
        lines = fh.read().strip().split("\n")

    records = []
    cancelled = 0

    for raw in lines:
        rec = parse_record(raw)
        if sales_tools.is_cancelled(rec["status"]):
            cancelled += 1
            continue
        records.append(rec)

    print(f"মোট লাইন: {len(lines)}টা  ·  বাতিল: {cancelled}টা  ·  হিসাবে: {len(records)}টা")
    print()

    totals, counts = totals_by(records, "item_name")

    print("পণ্য ধরে হিসাব")
    for name in sorted(totals):
        print(f"   {name:<20} {counts[name]}টা   {sales_tools.taka(totals[name])}")

    print(f"   {'সব মিলিয়ে':<20} {len(records)}টা   {sales_tools.taka(sum(totals.values()))}")
    print()

    top_item = max(totals, key=totals.get)
    print(f"সবচেয়ে বেশি বিক্রি: {top_item} — {sales_tools.taka(totals[top_item])} ({counts[top_item]}টা অর্ডার)")

    return records, totals, counts


if __name__ == "__main__":
    level_1()
