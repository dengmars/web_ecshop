from selenium.webdriver.common.by import By

from page.Base_page import BasePage
class HomePage(BasePage):
    keyword_locator=(By.CSS_SELECTOR, "#keyword") # 输入框

    search_locator=(By.CSS_SELECTOR, "#searchForm > span.ipt2 > input") # 搜索按钮

    clickshop_locator=(By.CSS_SELECTOR, "#compareForm > div > div:nth-child(1) > a > img") # 点击图片

    buy_locator=(By.CSS_SELECTOR, "#ECS_FORMBUY > ul.bnt_ul > li.padd > a > img") # 点击购买按钮


    settlement_locator=(By.CSS_SELECTOR,
                             "body > div.block.table > div.flowBox > table > tbody > tr > td:nth-child(2) > a > img")# 点击结算中心
    distribution_locator=(By.XPATH,"/html/body/div[7]/form[1]/div/table/tbody/tr[6]/td/input[1]")
    print("...........")




    def input_keyword(self,keyword):
        '''
        输入商品关键字
        :param keyword:
        :return:
        '''
        self.find_element(self.keyword_locator).send_keys(keyword)
    def input_search(self):
        '''
        点击搜索
        :return:
        '''
        self.find_element(self.search_locator).click()
    def input_clickshop(self):
        '''
        点击搜索出来的商品
        :return:
        '''
        self.find_element(self.clickshop_locator).click()
    def input_buy(self):
        '''
        点击购买
        :return:
        '''
        self.find_element(self.buy_locator).click()
    def input_settlement(self):
        '''
        点击结算中心
        :return:
        '''
        self.find_element(self.settlement_locator).click()
    def input_distribution(self):
        self.find_element(self.distribution_locator).click()
    def home(self,keyword):
        self.input_keyword(keyword)
        self.input_search()
        self.input_clickshop()
        self.input_buy()
        self.input_settlement()
        self.input_distribution()

