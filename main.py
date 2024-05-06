import pandas as pd
from ics import Calendar, Event
from datetime import datetime

# 从CSV文件读取数据并解析日期列
def read_csv(file_path):
    return pd.read_csv(file_path, parse_dates=['夏令营报名开始', '夏令营报名结束', '夏令营结果通知', '夏令营时间开始', '夏令营时间结束'])

# 解析日期，并添加默认的年份
def parse_date(date, default_year=2024):
    if pd.isnull(date):
        return None
    if isinstance(date, pd.Timestamp):
        return datetime.combine(date, datetime.min.time())
    # 如果日期已是datetime.date类型，直接组合
    date_str = f"{default_year}-{date}"
    return datetime.strptime(date_str, "%Y-%m-%d")

# 将CSV数据转换为ICS日历事件
def create_ics_file(data, output_file):
    calendar = Calendar()
    
    for index, row in data.iterrows():
        if pd.isnull(row['夏令营报名开始']) or pd.isnull(row['夏令营报名结束']):
            print(f"Skipping row {index + 1}: Missing necessary date information.")
            continue
        
        # 创建一个夏令营报名事件
        registration_event = Event()
        registration_event.name = f"{row['学校名字']} 夏令营报名"
        registration_event.begin = parse_date(row['夏令营报名开始'])
        registration_event.end = parse_date(row['夏令营报名结束'])
        registration_event.description = f"夏令营报名链接: {row['url']}"
        registration_event.location = row['学校名字']
        calendar.events.add(registration_event)

        # 检查其他日期
        if pd.isnull(row['夏令营结果通知']):
            print(f"Notice date missing in row {index + 1}. Skipping notification event.")
        else:
            # 创建一个夏令营结果通知事件
            notification_event = Event()
            notification_event.name = f"{row['学校名字']} 夏令营结果通知"
            notification_event.begin = parse_date(row['夏令营结果通知'])
            notification_event.description = "夏令营结果将会在今天通知。"
            notification_event.location = row['学校名字']
            calendar.events.add(notification_event)

        # 创建一个夏令营活动
        camp_event = Event()
        camp_event.name = f"{row['学校名字']} 夏令营活动"
        camp_event.begin = parse_date(row['夏令营时间开始'])
        camp_event.end = parse_date(row['夏令营时间结束'])
        camp_event.description = "参加夏令营活动。"
        camp_event.location = row['学校名字']
        calendar.events.add(camp_event)
        
    # 保存ICS文件
    with open(output_file, 'w') as my_file:
        my_file.writelines(calendar)

# 主函数
def main():
    csv_path = 'time.csv'  # CSV文件路径
    ics_output_path = 'school_camps.ics'  # 输出ICS文件名
    data = read_csv(csv_path)
    create_ics_file(data, ics_output_path)
    print("ICS日历文件已生成！")

if __name__ == "__main__":
    main()
