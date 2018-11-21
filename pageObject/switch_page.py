from common.base_page import BasePage
from utils.config import Config

class SwitchPage(BasePage):
    # for login
    menu_field='class_name,glyphicon-menu-hamburger'

    # for switch page
    def linkTo(self,pageName):
        page =Config().get(pageName)
        self.click(self.menu_field)
        self.click('link_text,'+page)