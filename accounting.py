
import pandas as pd
import numpy as np


def preprocessing():
    columns = ['bookingdate', 'valuta', '', 'company',
                'account', 'bank', 'subject', 'currency',
                'value', 'movement']


    data = pd.read_csv('data/test2.csv', names=columns, skiprows=1)

    def format_value(x):
        x = x.replace('.', '')
        return float(x.replace(',', '.'))

    data['value'] = data['value'].apply(format_value)
    return data



def get_spendings():
    d = preprocessing()
    return d.groupby('movement').get_group('S').sort('value')[['bookingdate', 'company', 'value']]


def get_detailed_spendings(str_):
    d = get_spendings()

    d['new'] = d.company.astype(str).map(lambda x: str_.lower() in x.lower())
    d = d.groupby('new').get_group(True)
    del d['new']
    return d


if __name__ == '__main__':
    print get_detailed_spendings('boulder')

"""
>>> total = d.groupby('movement').get_group('S')['value'].sum()
>>> fix = d.groupby('movement').get_group('S').sort('value')[['company', 'value']].ix[[2,20, 30]]['value'].sum()
>>> total -fix

"""
