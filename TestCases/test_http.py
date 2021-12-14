# -*- coding: utf-8 -*-
# @Time : 2020/10/26 23:53
# @Author : Liangjiajing
# @FileName: test_http.py
# @Email : 1369462217@qq.com
import unittest
from ddt import ddt,data
from Common.DoExcel import DoExcel
from Common.http_request import HttpRequest
from Common.dir_config import *
from Common.get_data import Data
from Common.myLogger import MyLogger
file_name = os.path.join(testdatas_dir, 'do_excel.xlsx')
test_data = DoExcel().do_excel(file_name,'teacher')
@ddt
class TestHttpRequest(unittest.TestCase):
    def setUp(self):
        pass
    @data(*test_data)
    def test_login_api(self,item):
        # print(item['url'],eval(item['data']),item['method'],getattr(Data,'Cookie'))
        res = HttpRequest().http_request(item['url'],eval(item['data']),item['method'],getattr(Data,'Cookie'))
        if res.cookies:
            setattr(Data,'Cookie',res.cookies)

        if str(res.json()).find('id') != -1:
            # setattr(Data,'id',res.json()['id'])
            # print(getattr(Data,'id'))
            print(res.json()['id'])
            print('------------------------------')
            DoExcel().get_id(str(res.json()['id']))
        try:

            self.assertEqual(item['msg'],res.json()['retcode'])
            TestResult = 'PASS'
        except AssertionError as e:
            TestResult = 'Failed'
            MyLogger().error('-------------断言失败-----------')
            raise e
        finally:
            DoExcel().write_back(file_name,'teacher',item['case_id']+1,str(res.json()),TestResult)

    def tearDown(self):
        pass