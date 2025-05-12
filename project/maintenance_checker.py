import csv
from datetime import datetime

log_file = "maintenance_log.csv"
seen_rows = set()
last_date = None

with open(log_file, "r") as f:
    reader = csv.DictReader(f)
    print("=== Maintenance Log Check ===\n")

    for row in reader:
        row_key = (row['Aircraft'], row['Date'], row['Task'], row['Engineer'])

        # Check for duplicates
        if row_key in seen_rows:
            print(f"[DUPLICATE] Entry repeated: {row}")
        else:
            seen_rows.add(row_key)

        # Check for missing engineer
        if row['Engineer'].strip() == "":
            print(f"[MISSING] Engineer name missing: {row}")

        # Check for suspicious gaps in maintenance
        try:
            current_date = datetime.strptime(row['Date'], "%Y-%m-%d")
            if last_date:
                gap = (current_date - last_date).days
                if gap > 10:
                    print(f"[WARNING] {gap} days gap between logs: {row['Date']} and {last_date.date()}")
            last_date = current_date
        except:
            print(f"[ERROR] Invalid date format: {row['Date']}")
