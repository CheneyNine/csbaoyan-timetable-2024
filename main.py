import pandas as pd
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import pytz

# 从CSV文件读取数据并解析日期列
def read_csv(file_path):
    return pd.read_csv(file_path, parse_dates=['夏令营报名开始', '夏令营报名结束', '夏令营结果通知', '夏令营时间开始', '夏令营时间结束'])

# 解析日期，并添加默认的年份
def parse_date(date, default_year=2024):
    if pd.isnull(date):
        return None
    if isinstance(date, pd.Timestamp):
        return datetime(default_year, date.month, date.day)
    date_str = f"{default_year}-{date}"
    return datetime.strptime(date_str, "%Y-%m-%d")

# 将CSV数据转换为ICS日历事件
def create_ics_file(data, output_file):
    calendar = Calendar()
    calendar.add('prodid', '-//Apple Inc.//macOS 14.4.1//EN')
    calendar.add('version', '2.0')
    calendar.add('calscale', 'GREGORIAN')
    calendar.add('method', 'PUBLISH')

    for index, row in data.iterrows():
        if pd.isnull(row['夏令营报名开始']) or pd.isnull(row['夏令营报名结束']):
            print(f"Skipping row {index + 1}: Missing necessary date information.")
            continue

        event = Event()
        event.add('summary', f"{row['学校名字']} 夏令营报名")
        event.add('dtstart', parse_date(row['夏令营报名开始']))
        event.add('dtend', parse_date(row['夏令营报名结束']) + timedelta(days=1))
        event.add('dtstamp', datetime.now(pytz.utc))
        event.add('transp', 'TRANSPARENT')
        event.add('uid', f"{index}@example.com")
        calendar.add_component(event)

    with open(output_file, 'wb') as my_file:
        my_file.write(calendar.to_ical())

# 主函数
def main():
    csv_path = 'time.csv'  # CSV文件路径
    ics_output_path = 'school_camps.ics'  # 输出ICS文件名
    data = read_csv(csv_path)
    create_ics_file(data, ics_output_path)
    print("ICS日历文件已生成！")

if __name__ == "__main__":
    main()
