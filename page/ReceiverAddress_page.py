from selenium.webdriver.common.by import By
from page.Base_page import BasePage
from selenium.webdriver.support.select import Select
from  time import sleep
class AddressPage(BasePage):
    address_locator=(By.CSS_SELECTOR,"body > div.block.clearfix > div.AreaL > div > div > div > div > a:nth-child(4)")
    state_locator=(By.CSS_SELECTOR,"#selCountries_0")  #selCountries_0
    province_locator=(By.CSS_SELECTOR,"#selProvinces_0") #selProvinces_0
    citylevel_locator=(By.ID, "selCities_0")  #selCities_0
    region_locator=(By.CSS_SELECTOR, "#selDistricts_0")  #selDistricts_0
    consignee_locator=(By.CSS_SELECTOR, "#consignee_0") # 收货姓名

    detailedaddress_locator=(By.CSS_SELECTOR, "#address_0")  # 详细地址

    phone_locator=(By.CSS_SELECTOR, "#tel_0")  # 电话

    email_locator=(By.CSS_SELECTOR, "#email_0")  # 电子邮件地址

    submit_locator=(By.CSS_SELECTOR,"body > div.block.clearfix > div.AreaR > div > div > div > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > input.bnt_blue_2")# 点击配送到这个地址

    def input_address(self):
        '''
        点击收货地址
        :return:
        '''
        self.find_element(self.address_locator).click()
    def input_state(self):
        '''
        选配送区域，选择国家
        :return:
        '''
        locator = self.find_element(self.state_locator)
        select = Select(locator)
        select.select_by_index(1)  # 配送区域
    def input_province(self):
        '''
        配送区域，选择省份
        :return:
        '''
        locator = self.find_element(self.province_locator)  # 配送区域
        select = Select(locator)
        select.select_by_index(1)
        sleep(2)

    def input_citylevel(self):
        '''
        配送区域，选择市级
        :return:
        '''
        locator = self.find_element(self.citylevel_locator)  # 配送区域
        select = Select(locator)
        select.select_by_index(1)
        sleep(2)
    def input_region(self):
        '''
        配送区域，选择区
        :return:
        '''
        locator = self.find_element(self.region_locator)  # 配送区域
        select = Select(locator)
        select.select_by_index(1)
    def input_consignee(self,consignee):
        '''
        输入收货人姓名
        :param
        :return:
        '''
        self.find_element(self.consignee_locator).send_keys(consignee)

    def input_detailedaddress(self, detailedaddress):
        '''
              输入详细地址
              :param
              :return:
              '''
        self.find_element(self.detailedaddress_locator).send_keys(detailedaddress)

    def input_phone(self, phone):
        '''
              输入手机号
              :param
              :return:
              '''
        self.find_element(self.phone_locator).send_keys(int(phone))

    def input_email(self, email):
        '''
              输入邮箱
              :param
              :return:
              '''
        self.find_element(self.email_locator).clear()
        self.find_element(self.email_locator).send_keys(email)
        sleep(2)
    def input_submit(self):
        '''
              点击新增
              :param
              :return:
              '''
        self.find_element(self.submit_locator).click()

    def address(self,consignee,detailedaddress,phone,email):

        self.input_address()
        self.input_state()
        self.input_province()
        self.input_citylevel()
        self.input_region()
        self.input_consignee(consignee)
        self.input_detailedaddress(detailedaddress)
        self.input_phone(phone)
        self.input_email(email)
        self.input_submit()


