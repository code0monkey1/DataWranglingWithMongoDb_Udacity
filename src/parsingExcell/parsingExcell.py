import xlrd

datafile="2013_ERCOT_Hourly_Load_Data.xls"
def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)


    sheet = workbook.sheet_by_index(0)

    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    cv = sheet.col_values(1, start_rowx=1, end_rowx=None)
    max_val = max(cv)
    min_val = min(cv)
    avj_val = sum(cv) / len(sheet_data)
    max_time = xlrd.xldate_as_tuple(sheet.cell_value(cv.index(max_val)+1, 0), 0)
    min_time = xlrd.xldate_as_tuple(sheet.cell_value(cv.index(min_val)+1, 0), 0)

    data = {
        'maxtime': (0, 0, 0, 0, 0, 0),
        'maxvalue': 0,
        'mintime': (0, 0, 0, 0, 0, 0),
        'minvalue': 0,
        'avgcoast': 0
    }

    data['maxtime'] = max_time
    data['maxvalue'] = max_val
    data['mintime'] = min_time
    data['minvalue'] = min_val
    data['avgcoast'] = avj_val

    return data




