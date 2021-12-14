# -*- coding: utf-8 -*-
# @Time : 2020/10/24 14:53
# @Author : Liangjiajing
# @FileName: http_request.py
# @Email : 1369462217@qq.com
import requests
from Common.myLogger import MyLogger


class HttpRequest:
    def http_request(self, url, data, method, cookie=None):
        # 1、判断是get还是post请求
        # 2、调用request相应的方法.url
        # 3、获取return返回值
        # 判断数据是否为空，不为空则转换成字典类型的数据
        try:
            # if data is not None:
            #     data = eval(data)
            if method.upper() == 'GET':
                res = requests.get(url, data, cookies=cookie)
                MyLogger().info('当前请求为get')
            elif method.upper() == 'POST':
                res = requests.post(url, data, cookies=cookie)
                MyLogger().info('当前请求为post')
            elif method.upper() == 'DELETE':
                res = requests.delete(url, data=data, cookies=cookie)
                MyLogger().info('当前请求为post')
            elif method.upper() == 'PUT':
                res = requests.put(url, data, cookies=cookie)
                MyLogger().info('当前请求为put')
            else:
                MyLogger().error("输入的请求方式不对")
        except Exception as e:
            MyLogger().error("请求报错了:{0}".format(e))
            raise e
        return res


if __name__ == '__main__':
    pass
