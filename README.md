## 基于pytest的seleniumpo模型封装
在开始使用本项目之前，强烈建议您先阅读本文档

### 目录
- Page：该目录用于存放所有页面对象，实际的操作全部封装在该目录的文件
- Page\\datas :该目录用于存放所有页面对象的xpath值
- TestCase：该目录用于存放测试用例，使用了pytest框架进行管理
- TestCase\\bin: 存放有关allure报告的cmd语句操作

### 重要文件
1. Page\\BasePage : 该文件封装了pageObject的公共方法
2. pytest.ini : 该文件为pytest启动初始化，实现对allure结果进行保存
3. config : 该文件封装了系统使用的主要变量，如登录网址以及系统之前的路径，没有做自动读取，需手动配置
4. Page\\conftest.py : 实现pytest用例中文显示
5. datas下的yml与Page下的page文件必须同名，才可以使用BasePage中的PageElement对象，例：UserPage.py--UserPage.yml，这样系统会在调用UserPage时自动读取同名yml里面的文件

### 使用说明
1. 在TestCase目录下使用cmd运行pytest
2. 自动化脚本运行完之后，报告会自动生成，在TestCase\\bin目录下运行openallureReport.bat

