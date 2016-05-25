import os
# https://docs.python.org/3/library/os.path.html
import datetime
# https://docs.python.org/3.5/library/datetime.html

cwd = os.getcwd()
print('cwd:',cwd)
print("getcwd == abspath('.'):", cwd == os.path.abspath('.'))
print("getcwd == isabs()",os.path.isabs(cwd))

#os.makedirs(os.path.join(cwd, 'test'))
os.makedirs(os.path.join(cwd, 'test', 'lala'))
# Note makedirs creates all necessary directories
print('Test/lala directories created!')

print('.\\test exists?:',os.path.exists(os.path.join(cwd, 'test')))
print('.\\test\\lala exists?:',os.path.exists(os.path.join(cwd, 'test','lala')))
print('.\\test\\foo exists?:',os.path.exists(os.path.join(cwd, 'test','foo')))

file = open(os.path.join(cwd,'test','bar.txt'),'w')
file.write(str(datetime.datetime.now()))
file.close()

file = open(os.path.join(cwd,'test','bar.txt'))
contents = file.read()
print('bar.txt contained:', contents)
file.close()

os.remove(os.path.join(cwd,'test','bar.txt'))
print('Test\\bar.txt deleted!')

os.rmdir(os.path.join(cwd, 'test', 'lala'))
os.rmdir(os.path.join(cwd, 'test'))
print('Test\\lala directories deleted!')

path = 'C:\\Windows\\System32\\calc.exe'
print('Example path:',path)
print('basename:',os.path.basename(path))
print('dirname:',os.path.dirname(path))
print('split:',os.path.split(path))

print('path.split(os.path.sep):',path.split(os.path.sep))



