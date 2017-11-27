import datetime
import calendar 

START_DATE = datetime.date(2017, 2, 13)
TOTAL_PTO = 25
PTO_DATES_TAKEN = [
    datetime.date(2017, 5, 26),
    datetime.date(2017, 6, 5),
    datetime.date(2017, 6, 6),
    datetime.date(2017, 6, 7),
    datetime.date(2017, 6, 8),
    datetime.date(2017, 6, 9),
    datetime.date(2017, 6, 29),
    datetime.date(2017, 6, 30),
    datetime.date(2017, 7, 3),
    datetime.date(2017, 7, 28),
    datetime.date(2017, 8, 21),
    datetime.date(2017, 9, 8),
    datetime.date(2017, 11, 24)
]

def pto_days_remaining():
    current_date = datetime.date(2018, 1, 24)
    days_in_year = 366 if calendar.isleap(current_date.year) else 365
    pto_accured_per_day = float(TOTAL_PTO) / float(days_in_year)

    print START_DATE
    if current_date.month < START_DATE.month and current_date.day < START_DATE.day:
        anniversary_date = START_DATE.replace(year=current_date.year - 1)
    else:
        anniversary_date = START_DATE.replace(year=current_date.year)

    print anniversary_date
    pto_accrued_to_date = (current_date - anniversary_date).days * pto_accured_per_day
    pto_accrued_to_date_remaining = pto_accrued_to_date - len(PTO_DATES_TAKEN)
    print "PTO ACCRUED TO DATE REMAINING: {}".format(pto_accrued_to_date_remaining)
    total_pto_remaining = TOTAL_PTO - len(PTO_DATES_TAKEN)
    print "TOTAL PTO REMAINING: {}".format(total_pto_remaining)

pto_days_remaining()
