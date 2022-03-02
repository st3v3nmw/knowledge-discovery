import csv

with open("Risk data - Risk data.csv", "r") as f:
    reader = csv.DictReader(f)
    with open("preprocessed.csv", "w") as out:
        writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in reader:
            gender = 0 if row['GENDER'] == 'f' else 1
            mortgage = 0 if row['MORTGAGE'] == 'y' else 1
            how_paid = 0 if row['HOWPAID'] == 'weekly' else 1

            age = int(row['AGE'])
            if 18<= age <= 34:
                age_band = 1
            else:
                age_band = 1
            
            income = int(row['INCOME'])
            if 15000<= income <= 30000:
                income_band = 1
            elif 30001 <= income <= 45000:
                income_band = 2
            else:
                income_band = 3

            kids = int(row['NUMKIDS'])
            if 0 <= kids <= 2:
                kids_band = 1
            else:
                kids_band = 2
            

            cards  = int(row['NUMCARDS'])
            if 0 <= cards <= 2:
                cards_band = 1
            elif 3 <= cards <=4:
                cards_band = 2
            else:
                cards_band = 3

            marital = row['MARITAL']
            if marital == 'single':
                marital = 1
            elif marital == 'married':
                marital = 2
            else:
                marital = 3

            storecar = int(row['STORECAR'])
            loans = int(row['LOANS'])
            risk = row['RISK']
            if risk == 'bad risk':
                risk =1
            elif risk == 'bad profit':
                risk = 2
            else: 
                risk = 3
            
            writer.writerow(
                {
                    "ID" : row["ID"],
                    "AGE": age_band,
                    "INCOME": income_band,
                    "GENDER": gender,
                    "MARITAL": marital,
                    "NUMKIDS": kids_band,
                    "NUMCARDS": cards_band,
                    "HOWPAID" : how_paid,
                    "MORTGAGE": mortgage,
                    "STORECAR": storecar,
                    "LOANS": loans,
                    "RISK": risk
                }
            )
            
