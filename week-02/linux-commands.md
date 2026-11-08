# Class 2 - Linux Commands

## 1. Count CSV and Log Lines

wc -l module-01/data/orders_oct2026.csv

wc -l module-01/data/app_2026-10.log

## 2. Filter Log Data

grep -c "| WARN" module-01/data/app_2026-10.log

grep -c "DEBUG" module-01/data/app_2026-10.log

grep "^2026-10-10" module-01/data/app_2026-10.log | grep -c "| ERROR |"

## 3. Extract and Count Data

grep "| WARN" module-01/data/app_2026-10.log | cut -c1-10 | sort | uniq -c | sort -rn

grep -ic "bkash" module-01/data/orders_oct2026.csv

## 4. Bonus Commands

grep "auth" module-01/data/app_2026-10.log | grep -c "| ERROR |"

grep "| ERROR |" module-01/data/app_2026-10.log | cut -c1-10 | sort | uniq -c | sort -n
