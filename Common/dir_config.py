# -*- coding: utf-8 -*-
# @Time : 2020/10/24 17:18
# @Author : Liangjiajing
# @FileName: dir_config.py
# @Email : 1369462217@qq.com
import os

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

report_dir = os.path.join(path,'HtmlTestReports')

logs_dir = os.path.join(path,'Logs')

testcases_dir = os.path.join(path,'TestCases')

testdatas_dir = os.path.join(path,'TestDatas')

config_dir = os.path.join(path,'conf','case_config')



