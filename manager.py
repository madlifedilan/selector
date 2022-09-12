import logging
import time
from concurrent.futures import *
from time import sleep

from login import Login
from seizer import Seizer


class Info:
    def __init__(self, data):
        self.tag = data["tag"]  # 标志
        self.username = data["username"]  # 学号
        self.password = data["password"]  # 密码
        self.courseId = data["courseId"]
        # self.cour_type = data["cour_type"]  # 抢课类型
        # self.value = data["teacher"]  # 老师姓名
        # self.index = data["index"]  # 相同老师姓名时选第几个


class CourseManager(object):
    thread_number = 1  # 进程数
    seizer_list = []
    server_url = ['http://127.0.0.1:8000'
                 ]  # 抢课服务器地址

    def __init__(self, info, thread_num=1):
        self.thread_number = thread_num
        self.info = info
        logging.info(self.info.tag)
        logging.info("学号:{}".format(self.info.username))
        # logging.info("抢课类型:{}".format(self.info.cour_type))
        logging.info("抢课序号:{}".format(self.info.courseId))

    def run(self):
        # sleep(2)
        login = Login(self.info.username, self.info.password, 100)
        # time.sleep(1)
        login.login()
        cookies = login.get_cookies()
        time.sleep(3)
        for n in range(self.thread_number):
            target_host = self.server_url[n % len(self.server_url)]
            self.seizer_list.append(Seizer(n, target_host, cookies, self.info, 100))

        with ThreadPoolExecutor(8) as executor:

            future_task = [executor.submit(seizer.seize_whole) for seizer in self.seizer_list]

            wait(future_task, return_when=FIRST_COMPLETED)  # 等待一个进程结束
            executor.shutdown()
