# This is a sample Python script.
import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    v_abd = 'CD'
    print(v_abd)
    ds = pd.read_excel('trans070323.xlsx', "trans070323")
    # print(ds.columns)
    # print(ds[['Date', 'Debit']][1:10])
    # print(ds.iloc[0:4])
    # print(ds.iloc[2, 1])

    # for index, row in ds.iterrows():
    #   print(row)
    # print(ds.loc[ds['Debit'] > 100])
    # print(ds.sort_values(['Credit', 'Debit'], ascending=[1,0]))
    ds['Credit'] = ds['Credit'].fillna(0)

    ds['Debit'] = ds['Debit'].fillna(0)
    ds['Total'] = ds['Credit'] + ds['Debit']
    print(ds.head(100))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
