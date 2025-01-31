import requests

# 基础URL
base_url = "http://218.204.129.252:8088/jwglxt/templete/scorePrint/"

# 学号范围和时间范围
student_id_range = range(240615600, 240215639)
a = range(10,20)
time_start = "2025-01-02_06_00_00"
time_end = "2025-01-02_18_00_00"
def check_file_exists(url):
    try:
        response = requests.head(url)
        # 检查状态码
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return False
# 检查文件是否存在的函数
def check_pdf_exists(file_url):
    try:
        response = requests.head(file_url)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"请求失败：{e}")
        return False

# 遍历学号和时间，检查每个文件是否存在
for i in a:
    print(i)
for student_id in [240615600,240615601]:
    print("a")
    for hour in range(6, 19):  # 从6点到18点
        for minute in range(0, 60):  # 每分钟
            for second in range(0, 60):  # 每秒
                date_time = f"2025-01-02_{hour:02}_{minute:02}_{second:02}"
                file_name = f"score_{student_id}_{date_time}.pdf"
                file_url = base_url + file_name
                if check_file_exists(file_url):
                    print(f"文件存在: {file_name}")
                else:
                    print(f"文件不存在（返回404）: {file_name}")