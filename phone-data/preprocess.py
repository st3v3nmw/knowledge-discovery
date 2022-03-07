import csv
from datetime import datetime

with open("phone-data.csv", "r") as f:
    reader = csv.DictReader(f)
    with open("preprocessed.csv", "w") as out:
        writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            gender = 0 if row['gender'] == 'F' else 1
            marital_status = 0 if row['marital status'] == 'single' else 1
            row['time of call'] = row['time of call'].replace('a.m', ' AM')
            row['time of call'] = row['time of call'].replace('p.m', ' PM')
            time_obj = datetime.strptime(row['time of call'], '%I:%M %p')

            age = int(row["Age (yrs)"])
            if 19 <= age <= 25:
                age_band = 1
            elif 26 <= age <= 35:
                age_band = 2
            elif 35 <= age <= 45:
                age_band = 3
            else:
                age_band = 4

            hr = time_obj.hour
            if hr < 6:
                time_band = 1
            elif hr < 8:
                time_band = 2
            elif hr < 12:
                time_band = 3
            elif hr < 14:
                time_band = 4
            elif hr < 17:
                time_band = 5
            elif hr < 20:
                time_band = 6
            elif hr < 22:
                time_band = 7
            else:
                time_band = 8

            writer.writerow({
                "transaction no.": row["transaction no."],
                "tel.no": row["tel.no"],
                "gender": gender,
                "marital status": marital_status,
                "Age (yrs)": age_band,
                "time of call": time_band,
                "length of call (sec)": row["length of call (sec)"]
            })
