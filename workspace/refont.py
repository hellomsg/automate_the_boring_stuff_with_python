#!python
# -*- coding: utf-8 -*-

import openpyxl
from openpyxl.styles import Font
wb = openpyxl.Workbook()
sheet = wb.get_sheet_by_name('Sheet')
italic24Font = Font(size=24, italic=True)
sheet.column_dimensions['A'].font = italic24Font
sheet['A1'] = 'Hello world!'
wb.save('styled.xlsx')
