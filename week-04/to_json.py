#!/usr/bin/env python3
import json
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
    cancelled = 0

    for raw in lines:
        rec = parse_record(raw)
        if sales_tools.is_cancelled(rec["status"]):
            cancelled += 1
            continue
        records.append(rec)

    return records, cancelled


def totals_by(records, key):
    totals = {}
    counts = {}
    for rec in records:
        name = rec[key]
        totals[name] = totals.get(name, 0.0) + rec["amount"]
        counts[name] = counts.get(name, 0) + 1
    return totals, counts


def main():
    records, cancelled = read_records()
    totals, counts = totals_by(records, "item_name")
    by_date, date_counts = totals_by(records, "order_date")

    os.makedirs(OUTDIR, exist_ok=True)
    path = os.path.join(OUTDIR, "report_week2.json")

    by_item = {name: round(total, 2) for name, total in sorted(totals.items())}
    by_date = {date: round(total, 2) for date, total in sorted(by_date.items())}

    top_item = max(totals, key=totals.get)

    report = {
        "company": "ThelaGari",
        "week": "2026-10-12 → 2026-10-18",
        "counted": len(records),
        "cancelled": cancelled,
        "grand_total": round(sum(totals.values()), 2),
        "top_item": {
            "item_name": top_item,
            "orders": counts[top_item],
            "total_amount": round(totals[top_item], 2),
        },
        "by_item": by_item,
        "by_date": by_date,
    }

    with open(path, "w", encoding="utf-8") as fh:
        json.dump(report, fh, ensure_ascii=False, indent=2)

    with open(path, "r", encoding="utf-8") as fh:
        report = json.load(fh)

    print(type(report["grand_total"]))
    print(report["top_item"]["item_name"])
    print(f"লেখা হলো: {path}")


if __name__ == "__main__":
    main()
