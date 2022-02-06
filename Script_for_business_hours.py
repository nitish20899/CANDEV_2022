# Code to get business hours 
from BusinessHours import BusinessHours as bh
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

def stat_holiday_but_not_weekend(date1,date2):
    delta = date2-date1
    all_dates = []
    for i in range(delta.days+1):
        day = date2 + timedelta(days=i)
        all_dates.append(day)
        
    holiday_count=0
    for date in all_dates:
        stat_holiday = date in Canada_holidays
        if weekend_or_not(date)==False and stat_holiday==True:
            holiday_count+=10
        else:
            pass
    
    return holiday_count*60


def business_hours(date1,date2):
    return (bh(date1,date2, worktiming=[7, 17], weekends=[6, 7]).getminutes()-stat_holiday_but_not_weekend(date1,date2))/60