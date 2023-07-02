import time

# 定义一个函数，用来打印当前时间，并暂停一段时间
def print_time():
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(current_time)
    time.sleep(60)  # 暂停 1 秒钟

# 循环打印当前时间，直到用户按下 Ctrl+C 停止程序
while True:
    print_time()
