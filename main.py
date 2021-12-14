# -*- coding: utf-8 -*-
# @Time : 2020/10/24 13:41
# @Author : Liangjiajing
# @FileName: main.py
# @Email : 1369462217@qq.com
from Common.http_request import HttpRequest
from Common.DoExcel import DoExcel
from Common.dir_config import *
from Common.get_data import Data
def run(test_data,file_name,sheet_name):
    for item in test_data:
        print(item['url'],eval(item['data']),item['method'])
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'],getattr(Data,'Cookie'))
        print(res.json())
        print(res.headers)
        if res.cookies:
            setattr(Data,'Cookie',res.cookies)
        DoExcel().write_back(file_name,sheet_name,item['case_id']+1,str(res.json()))

file_name = os.path.join(testdatas_dir, 'do_excel.xlsx')  #找到excel文件
test_data = DoExcel().do_excel(file_name,'login')
run(test_data,file_name,'login')