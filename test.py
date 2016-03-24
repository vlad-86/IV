import os
import shutil
import sys



sourceFile = "d:\Git\IV\IV"
destinationFile = "d:\GIT"

os.chdir(sourceFile)

#currentDir = os.getcwd().join('test.txt')

if os.path.exists(os.path.join(destinationFile, r'testtxt.txt')):
    os.remove(r'd:\GIT\testtxt.txt')


file = open(os.path.join(sourceFile,r'testtxt.txt'), 'w')
file.write('learning how to write and open file')
file.close()

shutil.move('testtxt.txt', 'd:\git')
os.startfile(os.path.join(destinationFile, r'testtxt.txt'))
