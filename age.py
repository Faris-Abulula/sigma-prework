import datetime

def age(date):
    current_year = datetime.datetime.now().year
    date = datetime.datetime.strptime(date, "%d-%m-%Y").year
    return current_year - date

print(age("01-01-1990"))
print(age("04-12-1972"))