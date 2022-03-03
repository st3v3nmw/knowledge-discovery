import pandas
pandas.options.mode.chained_assignment = None

data_frame = pandas.read_csv('datasets/risk_data.csv').dropna()

# remove the id column
data_frame.drop(['ID'], axis = 1, inplace = True) 

##########################    BIN CATEGORY SETTINGS       #################################
    # can be either 1 or 2

AGE_BIN = 1
INCOME_BIN = 1
KIDS_BIN = 1
CARDS_BIN = 1

for index in data_frame.index:
    # columns which need to be given numeric values

    gender = data_frame["GENDER"][index]
    married = data_frame["MARITAL"][index]
    paid = data_frame["HOWPAID"][index]
    mortgage = data_frame["MORTGAGE"][index]
    risk = data_frame["RISK"][index]

    age = data_frame["AGE"][index]
    income = data_frame["INCOME"][index]
    kids = data_frame["NUMKIDS"][index]
    cards = data_frame["NUMCARDS"][index]

    #gender column
    if gender == "m":
        data_frame["GENDER"][index] = 0
    elif gender == "f":
        data_frame["GENDER"][index] = 1
    # marital colum
    if married == "married":
        data_frame["MARITAL"][index] = 0
    elif married == "single":
        data_frame["MARITAL"][index] = 1
    elif married == "divsepwid":
        data_frame["MARITAL"][index] = 2
    # paid column
    if paid == "monthly":
        data_frame["HOWPAID"][index] = 0
    elif paid == "weekly":
        data_frame["HOWPAID"][index] = 1
    #mortgage column
    if mortgage == "y":
        data_frame["MORTGAGE"][index] = 0
    elif mortgage == "n":
        data_frame["MORTGAGE"][index] = 1

    #risk column
    if risk == "bad loss":
        data_frame["RISK"][index] = 0
    elif risk == "bad profit":
        data_frame["RISK"][index] = 1
    elif risk == "good risk":
        data_frame["RISK"][index] = 2

        #BINS
    # age bin
    if AGE_BIN == 1:
        if age >= 18 and age <= 34:
            data_frame["AGE"][index] = 0
        elif age >= 35 and age <= 50:
            data_frame["AGE"][index] = 1
    
    elif AGE_BIN == 2:
        if age >= 18 and age <= 25:
            data_frame["AGE"][index] = 2
        elif age >= 26 and age <= 34:
            data_frame["AGE"][index] = 3
        elif age >= 35 and age <= 50:
            data_frame["AGE"][index] = 4
    # income bin
    if INCOME_BIN == 1:
        if income >= 15000 and income <= 30000:
            data_frame["INCOME"][index] = 0
        elif income >= 30001 and income <= 45000:
            data_frame["INCOME"][index] = 1
        elif income >= 45001 and income <= 60000:
            data_frame["INCOME"][index] = 2

    if INCOME_BIN == 2:
        if income >= 15000 and income <= 29000:
            data_frame["INCOME"][index] = 3
        elif income >= 29001 and income <= 39000:
            data_frame["INCOME"][index] = 4
        elif income >= 39001 and income <= 60000:
            data_frame["INCOME"][index] = 5
    #kids bin
    #bin 1 : age remains as is in the origninal dataset
    if KIDS_BIN == 2:
        if kids >= 0 and income <= 2:
            data_frame["NUMKIDS"][index] = 5
        elif kids >= 3 and kids <= 4:
            data_frame["NUMKIDS"][index] = 6

    # cards bin
    if CARDS_BIN == 1:
        if cards >= 0 and cards <= 2:
            data_frame["NUMCARDS"][index] = 0
        elif cards >= 3 and cards <= 4:
            data_frame["NUMCARDS"][index] = 1
        elif cards >= 5 and cards <= 6:
            data_frame["NUMCARDS"][index] = 2

    if CARDS_BIN == 2:
        if cards >= 0 and cards <= 1:
            data_frame["NUMCARDS"][index] = 3
        elif cards >= 2 and cards <= 4:
            data_frame["INCOME"][index] = 4
        elif cards >= 5 and cards <= 6:
            data_frame["NUMCARDS"][index] = 5

# write the data to csv file
data_frame.to_csv('datasets/processed_risk_data.csv', index=False)

message = ''' \n\n Processed data written successfully to
\t relative path: datasets/processed_risk_data.csv\n\n '''

print(message)

