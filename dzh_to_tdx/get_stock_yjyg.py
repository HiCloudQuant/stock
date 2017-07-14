import tushare as ts
import csv
from collections import namedtuple

RowData = namedtuple('RowData', ['id', 'code', 'name', 'info', 'date', 'eps', 'detail'])


if __name__ == '__main__':
    # �����ļ�����
    data_file = 'r:\\test.csv'
    dzh_file = 'r:\\ҵ��Ԥ��.txt'
    txt_lines = []

    # ��ȡ����
    df = ts.forecast_data(2017, 2)
    df.to_csv(data_file)

    # ��ȡcsv
    with open(data_file, 'r') as f:
        reader = csv.reader(f)

        # ӳ�䵽namedtuple
        for row in map(RowData._make, reader):
            if len(row.id) > 0:
                dzh_code = f'SH{row.code}' if row.code.startswith('6') else f'SZ{row.code}'
                line = f'{dzh_code}\t{row.date} {row.info}: {row.detail}\n'
                txt_lines.append(line)

    with open(dzh_file, 'w') as f:
        f.writelines(txt_lines)