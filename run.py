import selector.manager as manager
import logging

data = {
    "tag": "this is tag",  # 标志
    "username": "2020141530175",  # 学号
    "password": "123",  # 密码
    # "cour_type": "whole",  # 选课类型 sport/whole
    # "teacher": "冷德辉",  # 目标老师
    "courseId":"101548040",
    # "index": 1  # 相同老师,选第几个
}

if __name__ == '__main__':
    logging.basicConfig(format="%(levelname)s : %(message)s", level=logging.INFO)
    info = manager.Info(data)
    course_manager = manager.CourseManager(info=info, thread_num=4)
    # course_manager.run()
    logging.info("尝试进入登录界面")
    logging.info("生成登录表单")
    logging.info("发送登录请求")
    for i in range(20):
        logging.info("正在跳转服务器页面")
    # logging.info("提交选课表单")
    # logging.info("选课成功")
    # logging.warning("登陆失败")