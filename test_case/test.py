
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

class testCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # get url from configFile
        url =Config().get('dev01_url')
        # get browserName from configFile
        browserName=Config().get("browserName")
        cls.browser= Browser(browserName)
        cls.browser.open_browser(url)
        cls.driver=cls.browser.driver

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
        tradeListPage=TradeListPage(self.driver)
        tradeListPage.selectEod()
        tradeListPage.searchDate("2018-11-08")

        try:
            self.assertEqual('2018-11-08',tradeListPage.getText())
            tradeListPage.save_screen_shot('tradeList_afterSearch')
        except Exception as e:
            print('Test Fail.', format(e))

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit_browser()


if __name__ == '__main__':
    unittest.main(verbosity=2) 