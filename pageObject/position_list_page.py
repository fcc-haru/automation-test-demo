from common.base_page import BasePage

class PositionListPage(BasePage):
    title_field='class_name,title-last'
    search_field='id,productNameFilterId'
    result_field='xpath,//*[@id="rmscomponent"]/app-rms-base/app-positions-browser/div/div/div[3]/table/tbody/tr[4]/td[3]'


    def typeSearch(self,productName):
        self.type_search(self.search_field,productName)
    
    def getText(self):
        return self.get_text(self.result_field)