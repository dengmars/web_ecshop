from selenium.webdriver.common.by import By
from page.Base_page import BasePage
class CenterPage(BasePage):

    dispatching_locator=(By.CSS_SELECTOR,"#shippingTable > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=radio]")  #点击配送方式
    pay_locator=(By.CSS_SELECTOR,"#paymentTable > tbody > tr:nth-child(2) > td:nth-child(1) > input[type=radio]") #点击支付方式

    submit_locator=(By.CSS_SELECTOR,"#theForm > div:nth-child(12) > div:nth-child(3) > input[type=image]:nth-child(1)") #点击提交订单

    def input_dispatching(self):
        '''
        选择配送方式
        :return:
        '''
        self.find_element(self.dispatching_locator).click()
    def input_pay(self):
        '''
        选择支付方式
        :return:
        '''
        self.find_element(self.pay_locator).click()
    def input_submit_(self):
        '''
        点击提交按钮
        :return:
        '''
        self.find_element(self.submit_locator).click()
    def center(self):
        self.input_dispatching()
        self.input_pay()
        self.input_submit_()