import os
from subprocess import call
from Migration import Migration
import sys
import shutil


vpcommon = "c:\VPProducts\ViewPoint\VPCommon"
sqllan16_path = os.environ['SQLANY16']

Migration.init_sybase_db()
test_dir = os.path.join(vpcommon, "T1844")
# os.chdir(%SQLANY16%)
# print("current directory is " + str(os.getcwd()))
# return_code = call("test.bat")

# print("execution finished - " + str(return_code))


# print("system path is - "+sqllan16_path)
# print("test file")
