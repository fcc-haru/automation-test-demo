# coding=utf-8
#1.先设置编码，utf-8可支持中英文，如上，一般放在第一行

#2.注释：包括记录创建时间，创建人，项目名称。
'''
Created on 2018-11-15
@author: zhangmin
Project:rms automation test
'''

#3.导入unittest等模块
import unittest,time
from time import sleep
import sys
sys.path.append(r'C:\Users\min.zhang\Desktop\rms-autotest')
from common.browser import Browser
from utils.config import Config
from pageObject.login_page import LoginPage
from pageObject.position_list_page import PositionListPage
from pageObject.switch_page import SwitchPage
from pageObject.trade_list_page import TradeListPage

#4.定义测试类，父类为unittest.TestCase。
class testCase(unittest.TestCase):
    #5.定义setUp()方法用于测试用例执行前的初始化工作。注意，所有类中方法的入参为self/cls，定义方法的变量也要“self.变量”
    @classmethod
    def setUpClass(cls):
        # get url from configFile
        url =Config().get('dev01_url')
        # get browserName from configFile
        browserName=Config().get("browserName")
        cls.browser= Browser()
        cls.browser.init_browser(browserName)
        cls.browser.open_browser(url)
        cls.driver=cls.browser.driver

    #6.定义测试用例，以“test_”开头命名的方法
    def test_login(self):
        loginPage = LoginPage(self.driver)
        loginPage.type_usermsg('rmstest01','Rmstest123')
        loginPage.send_submit_btn()
        sleep(3)
    
    def test_searchPro_positionList(self):
        positionListPage= PositionListPage(self.driver)
        #make sure in right page
        self.assertIn('positions-browser/list',self.driver.current_url)
        positionListPage.save_screen_shot('positionList_beforeSearch')
        #search productName
        positionListPage.typeSearch('EXA-X1147')
        sleep(2)
        try:
            self.assertIn('EXA-X1147',positionListPage.getText())
            positionListPage.save_screen_shot('positionList_afterSearch')
        except Exception as e:
            print('Test Fail.', format(e))
        
    def test_selectDate_tradeList(self):
        switchPage=SwitchPage(self.driver)
        tradeListPage=TradeListPage(self.driver)
        
        #switch to tradeList page
        switchPage.linkTo('tradeList')
        sleep(2)

        tradeListPage.save_screen_shot('tradeList_beforeSearch')
        #check EOD type and search date
        tradeListPage.selectEod()
        tradeListPage.searchDate("2018-11-08")
        sleep(2)
        try:
            self.assertEqual('2018-11-08',tradeListPage.getDateText())
            tradeListPage.save_screen_shot('tradeList_afterSearch')
        except Exception as e:
            print('Test Fail.', format(e))

    #7.定义tearDown()方法用于测试用例执行之后的善后工作。
    @classmethod
    def tearDownClass(cls):
        pass

#8如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__ == '__main__':
    unittest.main(verbosity=2) 