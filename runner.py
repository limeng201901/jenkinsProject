#! /usr/bin/env python
#coding=utf-8


import sys
import logging
import os
import pytest
import subprocess
import shutil

#Add src root dirctory to PYTHONPATH by extend sys.path
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))

fileHandler = logging.FileHandler(filename="./auto.log",encoding="utf-8")
logging.getLogger().setLevel(0)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')
fileHandler.setFormatter(formatter)

logging.getLogger().addHandler(fileHandler)


if __name__ == '__main__':
    logging.info("Start to execute  automation cases")


    #hand json
    #pytest.main(['-sq', 'testcases/contact/department/test_create_dep.py::TestCreateDep::test_create_new_dep_by_para'])
    pytest.main(['-sq','--alluredir','./testreport/xml', 'testcases'])
    # pytest.main(['-sq', './testcases'])

    #pytest.main(['-sq', 'testcases'])

    #pytest.main(['-sq', '--alluredir', 'testreport.bak', 'testcases/shoppingonline/test_update_shopping_info.py::TestUpdateShoppingInfo::test_1453775'])
    #print(subprocess.getstatusoutput('/usr/local/bin/allure generate --clean ../log/testreport/ -o ../log/testreport/html'))


    logging.info("End to execute APP UI automaction cases")
