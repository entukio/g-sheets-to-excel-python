import gspread
import pandas as pd

#file updater
sa = gspread.service_account(filename='service_account.json')
sheets = sa.open('List')
journal = sheets.worksheet('Journal')

range1 = journal.get('A1:F12')
lastrow = journal.row_count

#update cell
journal.update('A10','cz')

#update range
body=[31222, 4, 9,7,5,4,3,2,5,6,7,8,5,4,3,2,5,6,8,9,1] #the values should be a list
journal.append_row(body, table_range="A1:U")

