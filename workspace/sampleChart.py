#!python
# -*- coding: utf-8 -*-

import openpyxl
wb = openpyxl.Workbook()
sheet = wb.get_active_sheet()
for i in range(1, 10):
	sheet['A' + str(i)] = i

chart1 = openpyxl.chart.BarChart()
chart1.type = "col"
chart1.style = 10
chart1.title = "Bar Chart"
chart1.y_axis.title = 'Test number'
chart1.x_axis.title = 'Sample length (mm)'

data = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_row=10, max_col=1)
chart1.add_data(data, titles_from_data=False)
chart1.shape = 4
sheet.add_chart(chart1, "A10")

wb.save('sampleChart.xlsx')
