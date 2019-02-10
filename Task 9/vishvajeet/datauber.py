import pandas
import seaborn
data = pandas.read_csv('Desktop/uber-raw-data-apr14.csv')
data.tail()
data['Date/Time'] = data['Date/Time'].map(pandas.to_datetime)
data.tail()


def get_dom(dt):
    return dt.day

data['dom'] = data['Date/Time'].map(get_dom)

data.tail()
def get_weekday(dt):
    return dt.weekday()

data['weekday'] = data['Date/Time'].map(get_weekday)

def get_hour(dt):
    return dt.hour

data['hour'] = data['Date/Time'].map(get_hour)

data.tail()

hist(data.dom, bins=30, rwidth=.8, range=(0.5, 30.5))
xlabel('date of the month')
ylabel('frequency')
title('Frequency by DoM - uber - Apr 2014')

def count_rows(rows):
    return len(rows)

by_date = data.groupby('dom').apply(count_rows)
by_date

bar(range(1, 31), by_date)
