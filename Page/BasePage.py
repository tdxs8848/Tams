import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time

from Page.config import BaseConfig


class BasePage:
    def __init__(self, driver: WebDriver = None):
        print("正在初始化" + self.__class__.__name__ + "页面。。。")
        if driver is None:
            # 打开浏览器
            self.driver = webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
            # 最大化窗口
            self.driver.maximize_window()
            # 设置隐式等待时间
            self.driver.implicitly_wait(5)
            # 访问页面
            self.driver.get(self._base_url)
            print(self.__class__.__name__ + "页面开始测试...")
            # 读取页面对应的Element.yml文件
            self.PageElement = self.loadYaml(
                BaseConfig.PROJECTPATH + "Tams\\Page\\datas\\" + self.__class__.__name__ + ".yml")


        else:
            self.driver = driver
            # 读取页面对应的Element.yml文件
            self.PageElement = self.loadYaml(
                BaseConfig.PROJECTPATH + "Tams\\Page\\datas\\" + self.__class__.__name__ + ".yml")

    # 读取yaml文件
    def loadYaml(self, filename):
        with open(filename, encoding="utf-8") as f:
            Data = yaml.safe_load(f)
        return Data

    # def findElementXpath(self,ymlName):
    #     self.driver.find_element_by_xpath(self.Data.get(ymlName))

    def close(self):
        print(self.__class__.__name__ + "页面测试结束，等待三秒后关闭浏览器")
        # 强制等待十秒后关闭浏览器
        time.sleep(3)
        self.driver.quit()

    # 使用该方法的ObjectPage必须对PageElement进行赋值
    def findElementXpathYml(self, nameElement):
        return self.driver.find_element_by_xpath(self.PageElement.get(nameElement))
