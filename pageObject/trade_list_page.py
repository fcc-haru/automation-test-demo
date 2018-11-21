from common.base_page import BasePage
from utils.config import Config

class TradeListPage(BasePage):
    # EOD_field='selector_selector,.mat-radio-label'
    EOD_field='id,mat-radio-6'
    data_field='id,dataToday'
    dateResult_field='xpath,//*[@id="rmscomponent"]/app-rms-base/app-global-trade-blotter/div/div/div[4]/table/tbody/tr[4]/td[6]'
    menu_field='class_name,glyphicon-menu-hamburger'

    tradeNum_field='selector_selector,tr.filter-style-tr>th:nth-child(4)>input'
    tradeNum_result_field='xpath,//*[@id="rmscomponent"]/app-rms-base/app-global-trade-blotter/div/div/div[4]/table/tbody/tr[4]/td[4]/a'
    
    # for switch page
    def linkTo(self,pageName):
        page =Config().get(pageName)
        self.click(self.menu_field)
        self.click('link_text,'+page)
    
    def selectEod(self):
        self.click(self.EOD_field)

    def searchDate(self,date):
        self.type_search(self.data_field,date)

    def getDateText(self):
        return self.get_text(self.dateResult_field)

    def searchTradeNum(self,text):
        self.type_search(self.tradeNum_field,text)

    def getTradeNumText(self):
        return self.get_text(self.tradeNum_result_field)
    
    