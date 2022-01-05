from datetime import date, timedelta
from cls.word_variants import WordVarGen

def a():
    date_list = []

    start_date = date(2000, 1, 1) 
    end_date = date(2003, 12, 31)

    delta = end_date - start_date   # returns timedelta

    for i in range(delta.days + 1):
        day = start_date + timedelta(days=i)
        day = str(day).split("-")

        date_list.append(day[0]+day[1]+day[2])
        date_list.append(day[2]+day[1]+day[0])

    s = WordVarGen()

    print(s.word_variant_hashed(word="tenletters", salt="BtwuyC", dates=date_list))

a()