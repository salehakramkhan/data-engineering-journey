#!/usr/bin/env python3
import csv
import os
import sales_tools

PATH = os.path.join("module-04", "data", "raw_sales_week2.txt")
OUTDIR = os.path.join("week-04", "output")


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


def read_records():
    with open(PATH, encoding="utf-8") as fh:
        lines = fh.read().strip().split("\n")

    records = []
    for raw in lines:
        rec = parse_record(raw)
        if sales_tools.is_cancelled(rec["status"]):
            continue
        records.append(rec)
    return records


def totals_by(records, key):
    totals = {}
    counts = {}
    for rec in records:
        name = rec[key]
        totals[name] = totals.get(name, 0.0) + rec["amount"]
        counts[name] = counts.get(name, 0) + 1
    return totals, counts


def main():
    records = read_records()
    totals, counts = totals_by(records, "item_name")

    os.makedirs(OUTDIR, exist_ok=True)

    clean = os.path.join(OUTDIR, "sales_week2_clean.csv")
    summary = os.path.join(OUTDIR, "item_summary.csv")

    columns = [
        "order_id", "order_date", "customer_name", "item_name",
        "quantity", "amount", "payment", "status"
    ]

    with open(clean, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns)
        writer.writeheader()
        writer.writerows(records)

    summary_columns = ["item_name", "orders", "total_amount"]
    with open(summary, "w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=summary_columns)
        writer.writeheader()
        for name in sorted(totals):
            writer.writerow({
                "item_name": name,
                "orders": counts[name],
                "total_amount": round(totals[name], 2),
            })

    back = []
    with open(clean, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            row["quantity"] = int(row["quantity"])
            row["amount"] = float(row["amount"])
            back.append(row)

    print(f"লেখা হলো: {clean}  ({len(records)}টা সারি + হেডার)")
    print(f"লেখা হলো: {summary}       ({len(totals)}টা সারি + হেডার)")
    print()
    print(f"CSV থেকে ফেরত পড়লাম: {len(back)}টা record")

    total = sum(rec["amount"] for rec in back)
    print(f"সব মিলিয়ে: {sales_tools.taka(total)}")


if __name__ == "__main__":
    main()
