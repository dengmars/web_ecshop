from selenium import webdriver
from selenium.webdriver.common.by import By
from page.Base_page import BasePage


class UserinfPage(BasePage):
    account_locator = (By.CSS_SELECTOR, "body > div.top_nav > div > div > a:nth-child(4)")  # 点击我的账户

    userinfo_locator = (By.CSS_SELECTOR,
                        "body > div.block.clearfix > div.AreaL > div > div > div > div > a:nth-child(2)")  # 点击我的用户信息

    officephone_locator = (By.CSS_SELECTOR,
                           "body > div.block.clearfix > div.AreaR > div > div > div > form:nth-child(4) > table > tbody > tr:nth-child(6) > td:nth-child(2) > input")  # 清空办公电话

    submit_locator = (By.CSS_SELECTOR,
                      "body > div.block.clearfix > div.AreaR > div > div > div > form:nth-child(4) > table > tbody > tr:nth-child(11) > td > input.bnt_blue_1")  # 点击确认修改

    def input_account(self):
        '''
        点击我的账户
        :return:
        '''
        self.find_element(self.account_locator).click()

    def input_userinfo(self):
        '''
        点击用户信息
        :return:
        '''
        self.find_element(self.userinfo_locator).click()

    def input_officephone(self, officepone):
        '''
        清空办公电话，在输入新的办公电话
        :param officephone:
        :return:
        '''
        self.find_element(self.officephone_locator).clear()
        self.find_element(self.officephone_locator).send_keys(int(officepone[0]))

    def input_submit(self):
        '''
        点击确认修改
        :return:
        '''
        self.find_element(self.submit_locator).click()

    def userinfo(self, officephone):
        self.input_account()
        self.input_userinfo()
        self.input_officephone(officephone)
        self.input_submit()
