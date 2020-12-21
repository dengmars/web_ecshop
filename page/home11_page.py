# from selenium.webdriver.common.by import By
# from page.base_ECshoppage import BasePage
# from model.browser import
# from selenium import webdriver
#
#
# class HomePage(BasePage):  # 就是把这个里面find_element()继承过来了
#     xiansuo_loc = (By.LINK_TEXT, "线索")
#     kehu_loc = (By.LINK_TEXT, "客户")
#     shangji_loc = (By.LINK_TEXT, "商机")
#
#     def xiansuo(self):
#         self.find_element(self.xiansuo_loc).click()
#
#     def kehu(self):
#         self.find_element(self.kehu_loc).click()
#
#     def shangji(self):
#         self.find_element(self.shangji_loc).click()
#
#     def Caidan(self):
#         # lp = BrowserEngine()
#         # self.driver = lp.get_browser()
#
#         self.driver.switch_to.frame("menu-frame")
from selenium.webdriver.common.by import By
from time import sleep

from page.base_ECshoppage import BasePage
from selenium.webdriver.support.select import Select


class HomePage(BasePage):
    ShopManagement_loc = (By.CSS_SELECTOR, '#menu-ul > li.collapse.lis.ico_1')
    ShopLists_loc = (By.LINK_TEXT, '商品列表')
    AddNewShop_loc = (By.LINK_TEXT, '添加新商品')
    PromotionalManagement_loc = (By.CSS_SELECTOR, '#menu-ul > li.collapse.lis.ico_2')
    TakeTheTreasureSoldier_loc = (By.LINK_TEXT, '夺宝奇兵')
    OrderManagement_loc = (By.CSS_SELECTOR, '#menu-ul > li.collapse.lis.ico_3')
    OrderLists_loc = (By.LINK_TEXT, '订单列表')
    UserManagement_loc = (By.CSS_SELECTOR, '#menu-ul > li.collapse.lis.ico_7')
    UserLists_loc = (By.LINK_TEXT, '会员列表')
    ShopName_loc = (
        By.CSS_SELECTOR, '#general-table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]:nth-child(1)')
    addshopqueding_loc = (By.CSS_SELECTOR, '#tabbody-div > form > div > input:nth-child(2)')
    ShopClassification_loc = (By.NAME, 'cat_id')
    table_loc = (By.CSS_SELECTOR, '#listDiv > table:nth-child(1) > tbody')
    tr_loc = (By.TAG_NAME, 'tr')
    td_loc = (By.TAG_NAME, 'td')
    a_loc=(By.TAG_NAME,'a')
    ShopPrice_loc = (
        By.CSS_SELECTOR, '#general-table > tbody > tr:nth-child(6) > td:nth-child(2) > input[type=text]:nth-child(1)')
    EditSure_loc = (By.XPATH, '//*[@id="tabbody-div"]/form/div/input[2]')

    def Menu(self):
        '''
        菜单栏元素定位
        :return:
        '''
        self.driver.switch_to.frame("menu-frame")

    def ManagementCenter(self):
        '''
        右边的管理中心页面元素定位
        :return:
        '''
        self.driver.switch_to.frame("main-frame")

    def SP_ShopManagement(self):
        '''
        左边的菜单下面的商品管理元素定位
        :return:
        '''
        self.find_element(self.ShopManagement_loc).click()

    def SP_ShopLists(self):
        '''
        商品管理里面的商品列表元素定位
        :return:
        '''
        self.find_element(self.ShopLists_loc).click()

    def SP_AddNewShop(self):
        '''
        点击商品下面的添加新商品后跳出的页面中的添加新商品的按钮元素定位
        :return:
        '''
        self.find_element(self.AddNewShop_loc).click()

    def PM_PromotionalManagement(self):
        '''
        左边菜单栏的促销管理元素定位
        :return:
        '''
        self.find_element(self.PromotionalManagement_loc).click()

    def PM_TakeTheTreasureSoldier(self):
        '''
        促销管理下面的夺宝奇兵元素定位
        :return:
        '''
        self.find_element(self.TakeTheTreasureSoldier_loc).click()

    def OM_OrderManagement(self):
        '''
        左边菜单栏的订单管理元素定位
        :return:
        '''
        self.find_element(self.OrderManagement_loc).click()

    def OM_OrderLists(self):
        '''
        订单管理下面的订单列表元素定位
        :return:
        '''
        self.find_element(self.OrderLists_loc).click()

    def UM_UserlManagement(self):
        '''
        左边菜单栏的订单管理会员管理元素定位
        :return:
        '''
        self.find_element(self.UserManagement_loc).click()

    def UM_UserLists(self):
        '''
        会员管理下面的会员列表元素定位
        :return:
        '''
        self.find_element(self.UserLists_loc).click()

    def Parent(self):
        '''
        跳到上一层
        :return:
        '''
        self.driver.switch_to.parent_frame()

    def ShopName(self, ShopName):
        '''
        定义一个类，点击到添加新商品下面到用户名输入框元素定位
        '''
        element = self.find_element(self.ShopName_loc)
        element.clear()
        element.send_keys(ShopName)

    def ShopClassification(self):
        '''
        点击到添加新商品下面到商品分类下拉框元素定位
        :return:
        '''
        locator = self.find_element(self.ShopClassification_loc)
        select = Select(locator)
        return select.select_by_index(3)

    def AddShopOKsumbit(self):
        '''
        点击到添加新商品下面到确认按钮元素定位
        :return:
        '''
        self.find_element(self.addshopqueding_loc).click()

    def ShopPrice(self, Price):
        '''
        先清空添加新商品页面的本店售价，在输入数据
        :return:
        '''
        element = self.find_element(self.ShopPrice_loc)
        element.clear()
        element.send_keys(Price)

    def EditSure(self):
        '''
        这个是编辑商品页面的确认按钮
        :return:
        '''
        self.find_element(self.EditSure_loc).click()

    def View(self):
        self.Menu()
        self.SP_ShopManagement()
        self.SP_ShopLists()
        self.Parent()
        self.ManagementCenter()

    def AddShopCollection(self, ShopName):
        '''
        这个是在home页面上操作整合
        :return:
        '''
        self.Menu()
        self.SP_ShopManagement()
        self.SP_ShopLists()
        self.Parent()
        self.ManagementCenter()
        self.SP_AddNewShop()
        self.ShopName(ShopName)
        self.ShopClassification()
        self.AddShopOKsumbit()

    def ViewCollection(self, bianhao):

        self.Menu()
        self.SP_ShopManagement()
        self.SP_ShopLists()
        self.Parent()
        self.ManagementCenter()
        table_element = self.find_element(self.table_loc)
        sleep(2)
        tr_lists = table_element.find_elements(*self.tr_loc)
        print(tr_lists)
        sleep(2)
        tr_lists = tr_lists[2:]
        for tr in tr_lists:
            td_list = tr.find_elements(*self.td_loc)
            sleep(3)
            if td_list[2].text == bianhao:
                sleep(1)
                print(td_list[2].text)
                sleep(1)
                td_list[10].find_elements(*self.a_loc)[1].click()
                # td_list[10].find_element(By.CSS_SELECTOR,
                #                          '#listDiv > table:nth-child(1) > tbody > tr:nth-child(9) > td:nth-child(11) > a:nth-child(2)').click()


    def EditCollection(self, bianhao, Price):

        self.Menu()
        self.SP_ShopManagement()
        self.SP_ShopLists()
        self.Parent()
        self.ManagementCenter()
        table_element = self.find_element(self.table_loc)
        sleep(2)
        tr_lists = table_element.find_elements(*self.tr_loc)
        print(tr_lists)
        sleep(2)
        tr_lists = tr_lists[2:]
        for tr in tr_lists:
            td_list = tr.find_elements(*self.td_loc)
            sleep(3)
            if td_list[2].text == bianhao:
                sleep(1)
                print(td_list[2].text)
                sleep(1)
                td_list[10].find_elements(*self.a_loc)[1].click()
                print(111111111)
                break
        self.ShopPrice(Price)
        self.EditSure()

    def EditPriceQ(self, bianhao):

        sleep(1)
        table_element =self.find_element(self.table_loc)
        sleep(2)
        tr_lists = table_element.find_elements(*self.tr_loc)
        sleep(1)
        tr_lists = tr_lists[2:]
        for tr in tr_lists:

            td_list = tr.find_elements(*self.td_loc)

            if td_list[2].text == bianhao:
                print(td_list[2].text)

                td_list[10].find_elements(*self.a_loc)[0].click()#listDiv > table:nth-child(1) > tbody > tr:nth-child(6) > td:nth-child(11) > a:nth-child(2)
                sleep(3)                            #listDiv > table:nth-child(1) > tbody > tr:nth-child(6) > td:nth-child(11) > a:nth-child(2) > img
                # listDiv > table:nth-child(1) > tbody > tr:nth-child(6) > td:nth-child(11) > a:nth-child(1)
    def DeleteShop(self, bianhao):
        sleep(2)
        table_element = self.find_element(self.table_loc)
        sleep(2)
        tr_lists = table_element.find_elements(*self.tr_loc)
        sleep(3)
        tr_lists = tr_lists[2:]
        for tr in tr_lists:

            td_list = tr.find_elements(*self.td_loc)
            sleep(3)
            if td_list[2].text == bianhao:
                print(td_list[2].text)
                sleep(1)
                td_list[10].find_elements(*self.a_loc)[3].click()
                # listDiv > table:nth-child(1) > tbody > tr:nth-child(3) > td:nth-child(11) > a:nth-child(4)
                self.driver.switch_to.alert.accept()
                print(111111111)
                break
            sleep(3)
