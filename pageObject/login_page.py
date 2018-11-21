from common.base_page import BasePage
from utils.config import Config

class LoginPage(BasePage):
    # for login
    username_field='id,name'
    password_field='id,password'
    submitbtn_field='class_name,btn-success'

    def type_usermsg(self,username,password):
        self.type(self.username_field,username)
        self.type(self.password_field,password)
    
    def send_submit_btn(self):
        self.click(self.submitbtn_field)

