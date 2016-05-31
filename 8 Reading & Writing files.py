import os
# https://docs.python.org/3/library/os.path.html
import datetime
# https://docs.python.org/3.5/library/datetime.html

cwd = os.getcwd()
print('cwd:',cwd,'\n')
print("getcwd == abspath('.'):\n\t", cwd == os.path.abspath('.'))
print("getcwd == isabs()\n\t",os.path.isabs(cwd))

print("Stuff inside this folder:\n\t",os.listdir(cwd))
size = 0
for filename in os.listdir(cwd):
	size = size + os.path.getsize(os.path.join(cwd,filename))
print("CWD total size:\n\t",size)

if(os.path.exists(os.path.join(cwd,'test'))):
	print('Directory already exists, exiting!')
	exit()
#os.makedirs(os.path.join(cwd, 'test'))
os.makedirs(os.path.join(cwd, 'test', 'lala'))
# Note makedirs creates all necessary directories
print('Test\\lala directories created!')

print('.\\test exists?\n\t',os.path.exists(os.path.join(cwd, 'test')))
print('.\\test\\lala exists?\n\t',os.path.exists(os.path.join(cwd, 'test','lala')))
print('.\\test\\foo exists?\n\t',os.path.exists(os.path.join(cwd, 'test','foo')))

file = open(os.path.join(cwd,'test','bar.txt'),'w')
file.write(str(datetime.datetime.now()))
file.close()

file = open(os.path.join(cwd,'test','bar.txt'))
contents = file.read()
print('bar.txt contained:\n\t', contents)
file.close()

os.remove(os.path.join(cwd,'test','bar.txt'))
print('Test\\bar.txt deleted!')

os.rmdir(os.path.join(cwd, 'test', 'lala'))
os.rmdir(os.path.join(cwd, 'test'))
print('Test\\lala directories deleted!\n')

path = 'C:\\Windows\\System32\\calc.exe'
print('Example path:',path)
print('basename:',os.path.basename(path))
print('dirname:',os.path.dirname(path))
print('split:',os.path.split(path))

print('path.split(os.path.sep):',path.split(os.path.sep))



