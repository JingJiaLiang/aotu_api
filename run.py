# -*- coding: utf-8 -*-
# @Time : 2021/10/15 0:21
# @Author : Liangjiajing
# @FileName: run.py
# @Email : 1369462217@qq.com
from HTMLTestRunnerNew import HTMLTestRunner
import unittest
from Common.http_request import HttpRequest
from Common.dir_config import *
Suite = unittest.TestSuite()
loader = unittest.TestLoader()
Suite.addTests(loader.discover(testcases_dir,pattern='test_*.py'))
with open(report_dir + r'\autoTest_login_api.html',"wb") as file:
    runner = HTMLTestRunner(
        stream=file,
        title='自动化接口测试报告',
        tester="liangjiajing",
        description='单元测试报告',
    )
    runner.run(Suite)