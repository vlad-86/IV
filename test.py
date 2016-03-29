import os
import shutil
import sys
from subprocess import call
from Migration import Migration
import sys
import shutil



vpcommon = "c:\VPProducts\ViewPoint\VPCommon"
sqllan16_path = os.environ['SQLANY16']

sourceFile = r"d:\Git\IV\IV"
destinationFile = "d:\GIT"

# os.chdir(sourceFile)

#currentDir = os.getcwd().join('test.txt')

if os.path.exists(os.path.join(destinationFile, r'testtxt.txt')):
    os.remove(r'd:\GIT\testtxt.txt')


# file = open(os.path.join(sourceFile,r'testtxt.txt'), 'w')
# file.write('learning how to write and open file')
# file.close()

# shutil.move('testtxt.txt', 'd:\git')
# os.startfile(os.path.join(destinationFile, r'testtxt.txt'))

# print("result is -"+str(Migration.init_sybase_db()))
test_dir = os.path.join(vpcommon, "T1844")
# os.chdir(%SQLANY16%)
# print("current directory is " + str(os.getcwd()))
# return_code = call("test.bat")

# print("execution finished - " + str(return_code))

# print("system path is - "+sqllan16_path)
# print("test file")

