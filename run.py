# coding=utf-8
import unittest, time, os 
import sys
sys.path.append(r'C:\Users\min.zhang\Desktop\rms-autotest')
from utils import HTMLTestRunner
   
case_list = './test_case'

def creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_list,pattern='*.py', top_level_dir=None)

    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
        print(testunit)
    return testunit

alltestnames = creatsuite()

report_path = os.path.dirname(os.path.abspath(__file__)) + '\\report\\'
now = time.strftime("%Y%m%d-%H%M%S",time.localtime(time.time()))
report_name = report_path+now+'-result.html'

fp = open(report_name, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'rms automation test report',
        description=u'rms automation test report:'
    )

runner.run(alltestnames)
fp.close()