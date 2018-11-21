import os
from .file_reader import YamlReader

BASE_PATH=os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
CONFIG_PATH=os.path.join(BASE_PATH,'data','config.yml')
DRIVER_PATH=os.path.join(BASE_PATH,'dirvers')
REPORT_PATH=os.path.join(BASE_PATH,'report')
LOG_PATH=os.path.join(BASE_PATH,'log')

# get value in configData
class Config:
    def __init__(self,config=CONFIG_PATH):
        print('config path:',config)
        self.config=YamlReader(config).data

    def get(self,element,index=0):
        return self.config[index].get(element)
