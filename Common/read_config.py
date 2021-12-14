# -*- coding: utf-8 -*-
# @Time : 2020/11/18 22:29
# @Author : Liangjiajing
# @FileName: read_config.py
# @Email : 1369462217@qq.com
import configparser
from Common.dir_config import *
class ReadConfig:
    @staticmethod
    def get_config(file_path,section,option):
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf.get(section,option)
if __name__ == '__main__':
    print(ReadConfig.get_config(config_dir,'MYSQL','mysql'))

