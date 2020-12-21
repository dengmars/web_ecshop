# from selenium.webdriver.common.by import By
# from page.base_CRMpage import BasePageCrm
#
#
#
# class LoginPage(BasePageCrm):
#     login_username_loc = (By.NAME, "name")
#     login_password_loc = (By.NAME, "password")
#     login_button = (By.NAME, "submit")
#
#
#     def input_username(self, username):
#         element = self.driver.find_element(*self.login_username_loc)
#         element.clear()
#         element.send_keys(username)
#
#
#     def input_password(self, password):
#         element = self.driver.find_element(*self.login_password_loc)
#         element.clear()
#         element.send_keys(password)
#
#
#     def submit(self):
#         self.driver.find_element(*self.login_button).click()
#
#
#     def login(self, username, password):
#         self.url()
#         self.input_username(username)
#         self.input_password(password)
#         self.submit()
from selenium.webdriver.common.by import By  # 引入By类
from page.Base_page import BasePage
from time import sleep  # 引入时间
class login1page(BasePage):
    url = BasePage.url + "/admin/"
    # 重写url属性，父类的url+/crm拼接

    # 页面属性
    # 用户名输入框定位器
    username_locator = (By.NAME, "username")
    # 密码输入框定位器
    password_locator = (By.NAME, "password")
    # 登录按钮定位器
    submit_locator = (By.CSS_SELECTOR,"input[value='进入管理中心']")

    def input_uesrname(self, username):  # 定义一个类，用于找到用户名输入框并进行输入
        element = self.driver.find_element(*self.username_locator)
        element.clear()
        element.send_keys(username)
        sleep(2)  # 暂时2秒

    def input_password(self, password):  # 定义一个类，用于找到密码输入框并进行输入
        element = self.driver.find_element(*self.password_locator)
        element.clear()
        element.send_keys(password)
        sleep(3)

    def sumbit(self):  # 定义一个类，用于找到按钮并点击
        self.driver.find_element(*self.submit_locator).click()
        sleep(3)

    def login(self, username, passwrod):  # 定义一个类，用于进行登录的一些操作
        # self.open()
        self.input_uesrname(username)
        self.input_password(passwrod)
        self.sumbit()





