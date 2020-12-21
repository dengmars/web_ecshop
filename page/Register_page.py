from selenium import webdriver
from selenium.webdriver.common.by import By
from page.Base_page import BasePage
class RegisterPage(BasePage):

    register_locator=(By.CSS_SELECTOR, "#ECS_MEMBERZONE > a:nth-child(1)") # 点击登录
    username1_locator=(By.CSS_SELECTOR,
                             "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input")# 输入用户名
    password1_locator=(By.CSS_SELECTOR,
                             "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > input")# 输入密码
    submit1_locator=(By.CSS_SELECTOR,
                             "body > div.block.block1 > div.usBox.clearfix > div.usBox_1.f_l > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input.us_Submit")  # 点击登录按钮
    def input_register(self):
        '''
        点击登录
        :return:
        '''
        self.find_element(self.register_locator).click()
    def input_username(self,username):
        '''
        输入用户名
        :param username:
        :return:
        '''
        self.find_element(self.username1_locator).send_keys(username)
    def input_password(self,password):
        '''
        输入密码
        :param password:
        :return:
        '''
        self.find_element(self.password1_locator).send_keys(password)
    def input_submit(self):
        '''
        点击登录按钮
        :return:
        '''
        self.find_element(self.submit1_locator).click()
    def register(self,username,password):

        self.input_register()
        self.input_username(username)
        self.input_password(password)
        self.input_submit()




