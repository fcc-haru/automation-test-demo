# 用于文件的读取,包含配置文件和数据文件的读取函数.根据文件地址，返回文件中包含的内容

import yaml
import os
from xlrd import open_workbook

# 读取配置文件yaml文件成配置内容
class YamlReader:
    def __init__(self, yamlfilepath):
        if os.path.exists(yamlfilepath):
            self.yamlfilepath = yamlfilepath
        else:
            raise FileNotFoundError('文件不存在！')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlfilepath, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))  # load后是个generator，用list组织成列表

        return self._data

# if __name__ == '__main__':
#     y = 'C:\\Users\\min.zhang\\Desktop\\rms-seleniumTest\\rms\data\\config.yml'
#     reader = YamlReader(y)
#     print(reader.data)
