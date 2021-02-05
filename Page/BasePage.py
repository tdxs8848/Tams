import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
class BasePage:
    def __init__(self,driver:WebDriver=None):
        print("正在初始化"+self.__class__.__name__+"页面。。。")
        if driver is None:
            #打开浏览器
            self.driver =webdriver.Chrome(executable_path="../Driver/chromedriver.exe")
            #最大化窗口
            self.driver.maximize_window()
            #设置隐式等待时间
            self.driver.implicitly_wait(5)
            #访问页面
            self.driver.get(self._base_url)
            print(self.__class__.__name__+"页面开始测试...")
        else:
            self.driver = driver

#注意该位置多文件后是否会出现问题
    #读取yaml文件
    def loadYaml(self,filename):
        with open(filename,encoding="utf-8") as f:
            Data = yaml.safe_load(f)
        return Data

    # def findElementXpath(self,ymlName):
    #     self.driver.find_element_by_xpath(self.Data.get(ymlName))

    def close(self):
        print(self.__class__.__name__+"页面测试结束，等待五秒后关闭浏览器")
        #强制等待十秒后关闭浏览器
        time.sleep(5)
        self.driver.quit()





