#coding:utf-8
import pytest
import allure
from selenium import webdriver
import time

@allure.feature("好爸爸hhhhhhhh")
class Testjenkins:
 def test_jenkins_pytest(self):
   with allure.step("测试hhhhhhhhhhh"):
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")