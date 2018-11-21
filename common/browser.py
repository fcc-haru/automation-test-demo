import sys
sys.path.append(r'C:\Users\min.zhang\Desktop\rms-autotest')
import time,os
from selenium import webdriver
from utils.config import DRIVER_PATH,REPORT_PATH
from selenium.webdriver.common.by import By
# from testCase.pageObject.pageLocator import PageLocator 

CHROMEDRIVER_PATH=DRIVER_PATH+'\chromedriver.exe'

TYPES = {'firefox': webdriver.Firefox, 'chrome': webdriver.Chrome, 'ie': webdriver.Ie, 'phantomjs': webdriver.PhantomJS}
EXECUTABLE_PATH = {'firefox': 'wires', 'chrome': CHROMEDRIVER_PATH}

class UnSupportBrowserTypeError(Exception):
    pass

class Browser(object):
    def __init__(self,browser_type="chrome"):
        self._type=browser_type.lower()
        if self._type in TYPES:
            browserObj=TYPES[self._type]
            self.browser=browserObj(EXECUTABLE_PATH[self._type])
        else:
            raise UnSupportBrowserTypeError('Just support %s!' % ','.join(TYPES.keys()))
        self.driver=None
    
    def open_browser(self,url,maximiza_window=True,implicitly_wait=30):
        self.driver = self.browser
        self.driver.get(url)
        if maximiza_window:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def close_browser(self):
        self.browser.close()

    def quit_browser(self):
        self.browser.quit()

if __name__ == '__main__':
    b=Browser('chrome')
    # test for baidu screenshot
    # b.get('https://www.baidu.com/')
    # b.save_screen_shot('test_baidu')

    # test for rms login
    # b.open_browser('http://d2-rms-web001.sbisec.int')
    # b.login_rms()
    # time.sleep(3)
    # b.quit()