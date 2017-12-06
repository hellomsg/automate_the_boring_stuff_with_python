#!python
# -*- coding: utf-8 -*-

import openpyxl, base_path

wb = openpyxl.load_workbook(base_path.files + '/produceSales.xlsx')
sheet = wb.get_active_sheet()
sheet.freeze_panes = 'A2'
wb.save('freezeExample.xlsx')
