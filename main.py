from ics import Calendar, Event
from datetime import datetime, timedelta

# 创建一个新的日历
c = Calendar()

# 定义添加事件的函数
def add_event(name, start, end, location):
    e = Event()
    e.name = name
    e.begin = start
    e.end = end
    e.location = location
    c.events.add(e)

# 设定开始日期
base_date = datetime(2023, 7, 28)  # 假设2023年7月28日是日程的开始日期

# 定义每个事件的时间信息
events = [
    ("Opening Ceremony", base_date + timedelta(hours=8, minutes=30), base_date + timedelta(hours=10, minutes=0), "E10-205"),
    ("Welcome Dinner (inc. Ice-breakers)", base_date + timedelta(hours=18, minutes=0), base_date + timedelta(hours=20, minutes=0), "E2-224"),
    ("Stan Z. Li - AI for Life Science", base_date + timedelta(days=2, hours=8, minutes=30), base_date + timedelta(days=2, hours=10, minutes=0), "E10-205"),
    ("Taiwen Tian - AI for scientific simulation and design", base_date + timedelta(days=2, hours=10, minutes=15), base_date + timedelta(days=2, hours=11, minutes=45), "E10-205"),
    ("Yulan He - Machine Reading Comprehension with Large Language Models-Part A", base_date + timedelta(days=2, hours=14, minutes=0), base_date + timedelta(days=2, hours=15, minutes=30), "E10-205"),
    ("Yulan He - Machine Reading Comprehension with Large Language Models-Part A", base_date + timedelta(days=2, hours=16, minutes=0), base_date + timedelta(days=2, hours=17, minutes=30), "E10-205"),
    ("Tao Cheng - Network and Graph based SpaceTimeAI for Smart Cities", base_date + timedelta(days=3, hours=8, minutes=30), base_date + timedelta(days=3, hours=10, minutes=0), "E10-205"),
    ("Hangzhou City Tour", base_date + timedelta(days=4, hours=9, minutes=0), base_date + timedelta(days=4, hours=17, minutes=30), "Hangzhou"),
    ("Panel - Forging New Frontiers with AI", base_date + timedelta(days=5, hours=8, minutes=30), base_date + timedelta(days=5, hours=10, minutes=0), "E10-205"),
    ("Zheng Zhang - Large Language Models: Working Mechanisms and Limitations", base_date + timedelta(days=5, hours=10, minutes=15), base_date + timedelta(days=5, hours=11, minutes=45), "E10-205"),
    ("Zheng Zhang - GAI for Science and Education Reform", base_date + timedelta(days=5, hours=14, minutes=0), base_date + timedelta(days=5, hours=15, minutes=30), "E10-205"),
    ("Poster Session", base_date + timedelta(days=5, hours=16, minutes=0), base_date + timedelta(days=5, hours=17, minutes=30), "E2-224"),
    ("Qiang Shen - Harnessing AI with Limited Data: Knowledge Interpolation and Practical Applications", base_date + timedelta(days=8, hours=8, minutes=30), base_date + timedelta(days=8, hours=10, minutes=0), "E10-205"),
    ("Bo Zhang - Fundamentals of 3D Generative Models and Recent Advances", base_date + timedelta(days=8, hours=10, minutes=15), base_date + timedelta(days=8, hours=11, minutes=45), "E10-205"),
    ("Qiang Shen - Enhancing Data Modeling and Analysis through Approximate Feature Selection", base_date + timedelta(days=8, hours=14, minutes=0), base_date + timedelta(days=8, hours=15, minutes=30), "E10-205"),
    ("Zhenchang Lan - Discovering the Intersection of AI Research", base_date + timedelta(days=8, hours=15, minutes=45), base_date + timedelta(days=8, hours=17, minutes=15), "E10-205"),
    ("Marios M. Polycarpou - Optimization Methods for AI", base_date + timedelta(days=9, hours=8, minutes=30), base_date + timedelta(days=9, hours=10, minutes=0), "E10-205"),
    ("Bing Liu - Continual Learning", base_date + timedelta(days=9, hours=10, minutes=15), base_date + timedelta(days=9, hours=11, minutes=45), "E10-205"),
    ("Marios M. Polycarpou - Machine Learning for Monitoring and Control of Cyber-Physical Systems", base_date + timedelta(days=9, hours=14, minutes=0), base_date + timedelta(days=9, hours=15, minutes=30), "E10-205"),
    ("Simon Yang - Bio-Inspired Intelligence with Applications to Diversified Robotic Systems-I", base_date + timedelta(days=10, hours=8, minutes=30), base_date + timedelta(days=10, hours=10, minutes=0), "E10-205"),
    ("Bing Liu - Autonomous Learning Agents", base_date + timedelta(days=10, hours=10, minutes=15), base_date + timedelta(days=10, hours=11, minutes=45), "E10-205"),
    ("Simon Yang - Bio-Inspired Intelligence with Applications to Diversified Robotic Systems-II", base_date + timedelta(days=10, hours=14, minutes=0), base_date + timedelta(days=10, hours=15, minutes=30), "E10-205"),
    ("Shiyu Zhao - From Bearing-Only to Bearing-X: Vision-Based Target Motion Estimation", base_date + timedelta(days=11, hours=10, minutes=15), base_date + timedelta(days=11, hours=11, minutes=45), "E10-205"),
    ("Yuchun Ma - From Multi-Objective Optimization to Multi-Objective Machine Learning", base_date + timedelta(days=11, hours=10, minutes=30), base_date + timedelta(days=11, hours=12, minutes=0), "E10-205"),
    ("Mengjie Zhang - Evolutionary Machine Learning Methods, Applications and Challenges", base_date + timedelta(days=11, hours=14, minutes=0), base_date + timedelta(days=11, hours=15, minutes=30), "E10-205"),
    ("Group Presentations and Awards Ceremony", base_date + timedelta(days=11, hours=14, minutes=0), base_date + timedelta(days=11, hours=15, minutes=30), "E10-205"),
    ("Farewell Dinner", base_date + timedelta(days=11, hours=18, minutes=0), base_date + timedelta(days=11, hours=20, minutes=0), "Floor 2, C7"),
]

# 添加所有事件到日历
for event in events:
    add_event(event[0], event[1], event[2], event[3])

# 保存日历到 .ics 文件
with open('program_schedule.ics', 'w') as f:
    f.writelines(c)

print("ICS 文件已生成：program_schedule.ics")
