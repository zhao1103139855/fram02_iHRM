"""

"""
# 1.导包
import logging
import unittest
import requests

import app
from api.EmpAPI import EmpCRUD


# 2.创建测试类


class Test_Emp(unittest.TestCase):

    # 3.初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUD()

    # 4.资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5.测试函数1：增
    # 直接执行该测试函数失败，为什么？
    # 原因：1.先执行登陆操作  2.还需要提交银行卡（token）
    # 解决：1.使用测试套件组织接口的执行顺序
    #     2.如何提交银行卡，如何实现关联？
    #        核心步骤1：token的提取
    #        核心步骤2：token的提交
    def test_add(self):
        logging.info("新增员工信息")
        # 1.请求业务
        response = self.emp_obj.add(self.session, username="wahaha88",
                                    mobile="13100019990")
        # 2.断言业务
        print("员工新增响应结果:", response.json())
        id = response.json().get("data").get("id")
        app.USER_ID = id
        print("新增员工的ID:", id)

        self.assertEqual(True,response.json().get("success"))
        self.assertEqual(10000,response.json().get("code"))
        self.assertIn("操作成功",response.json().get("message"))

    # 6.测试函数2：改
    def test_update(self):
        logging.warning("修改员工信息")
        # 1.请求业务
        response = self.emp_obj.update(self.session, app.USER_ID, "aotuman7417747")
        # 2.断言业务
        print("修改后的员工信息:", response.json())

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 7.测试函数3：查
    def test_get(self):
        logging.info("获取员工信息")
        # 1.请求业务
        response = self.emp_obj.get(self.session, app.USER_ID)
        # 2.断言业务
        print("-"*100)
        print("修改后的员工信息:", response.json())

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    # 8.测试函数4：删
    def test_delete(self):
        logging.warning("删除员工信息")
        #1.请求业务
        response = self.emp_obj.delete(self.session,app.USER_ID)
        # 2.断言业务
        print("-" * 100)
        print("删除成功后的数据:", response.json())

        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))


