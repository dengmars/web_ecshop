from selenium.webdriver.common.by import By
from page.Base_page import BasePage
from selenium import webdriver
from selenium.webdriver.support.select import Select
class LoginPage(BasePage):

    login_locator = (By.CSS_SELECTOR, "#ECS_MEMBERZONE > a:nth-child(2)")  # 点击注册
    username_locator = (By.CSS_SELECTOR, "#username") # 输入用户名
    email_locator = (By.CSS_SELECTOR, "#email")  # 输入邮箱
    password_locator = (By.CSS_SELECTOR, "#password1") # 输入密码
    passwd_locator = (By.CSS_SELECTOR, "#conform_password")# 确认密码
    msn_locator = (By.CSS_SELECTOR,
                                      "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > input") # 输入MSN
    qq_locator = (By.CSS_SELECTOR,
                                     "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(7) > td:nth-child(2) > input") # 输入qq
    officephone_locator = (By.CSS_SELECTOR,
                                              "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(8) > td:nth-child(2) > input")# 输入办公电话
    hometelephone_locator = (By.CSS_SELECTOR,
                                                "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(9) > td:nth-child(2) > input") # 输入家庭电话
    phone_locator = (By.CSS_SELECTOR,
                                        "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(10) > td:nth-child(2) > input")# 输入手机
    security_question_locator =(By.CSS_SELECTOR,
                                  "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(11) > td:nth-child(2) > select")  # 选择密保问题
    encrypted_answersn_locator = (By.CSS_SELECTOR,
                                       "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(12) > td:nth-child(2) > input") # 输入密保答案
    submit_locator = (By.CSS_SELECTOR,
                                         "body > div.block.block1 > div.usBox > div.usBox_1.f_l > form > table > tbody > tr:nth-child(14) > td:nth-child(2) > input.us_Submit_reg")

    def input_login(self):
        '''
        点击登录
        :return:
        '''
        self.find_element(self.login_locator).click()

    def input_username(self,username):
        '''
        输入用户名
        :param username:
        :return:
        '''
        self.find_element(self.username_locator).send_keys(username)

    def input_email(self,email):
        '''

        :param email: 输入邮箱
        :return:
        '''
        self.find_element(self.email_locator).send_keys(email)

    def input_password(self,password):
        '''
        输入密码
        :param password:
        :return:
        '''
        self.find_element(self.password_locator).send_keys(password)

    def input_passwd(self, passwd):
        '''
        输入确认密码
        :param passwd:
        :return:
        '''
        self.find_element(self.passwd_locator).send_keys(passwd)

    def input_msn(self,msn):
        '''
        输入msn
        :param msn:
        :return:
        '''
        self.find_element(self.msn_locator).send_keys(msn)

    def input_qq(self,qq):
        '''
        输入qq号 函数方法
        :param qq:
        :return:
        '''
        self.find_element(self.qq_locator).send_keys(int(qq))

    def input_officephone(self,officephone):
        '''
        输入办公电话
        :param officephone:
        :return:
        '''
        self.find_element(self.officephone_locator).send_keys(int(officephone))

    def input_hometelephone(self, hometelephone):
        '''
        输入家庭电话
        :param hometelephone:
        :return:
        '''
        self.find_element(self.hometelephone_locator).send_keys(int(hometelephone))

    def input_phone(self,phone):
        '''
        输入手机号
        :param phone:
        :return:
        '''
        self.find_element(self.phone_locator).send_keys(int(phone))

    def input_security_question(self):
        '''
        选择密保问题
        :return:
        '''
        locator=self.find_element(self.security_question_locator)
        select = Select(locator)
        select.select_by_index(1)

    def input_encrypted_answersn(self,answersn):
        '''
        输入密保答案
        :param daan:
        :return:
        '''
        self.find_element(self.encrypted_answersn_locator).send_keys(answersn)
    def input_submit(self):
        '''
        点击注册
        :return:
        '''
        self.find_element(self.submit_locator).click()
    def login(self,username,email,password,passwd,msn,qq,officephone,hometelephone,phone,encrypted_answern):
        self.open()
        self.input_login()
        self.input_username(username)
        self.input_email(email)
        self.input_password(password)
        self.input_passwd(passwd)
        self.input_msn(msn)
        self.input_qq(qq)
        self.input_officephone(officephone)
        self.input_hometelephone(hometelephone)
        self.input_phone(phone)
        self.input_security_question()
        self.input_encrypted_answersn(encrypted_answern)
        self.input_submit()





















