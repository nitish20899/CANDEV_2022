import holidays
Canada_holidays = holidays.Canada()
def weekend_or_not(date):
    if date.weekday() > 4:
        return True
    else:
        return False


from datetime import timedelta
def difference_dates(date1,date2):
    delta = date2-date1
    all_dates = []
    for i in range(delta.days+1):
        day = sdate + timedelta(days=i)
        all_dates.append(day)
    holiday_count=0
    for date in all_dates:
        stat_holiday = date in Canada_holidays
        if weekend_or_not(date)==True or stat_holiday==True:
            holiday_count+=1
        else:
            pass
    holidays_seconds = holiday_count * 24 * 60 * 60
    delta = delta.total_seconds()-holidays_seconds
    return float(delta/3600)