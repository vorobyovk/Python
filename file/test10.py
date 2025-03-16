import sys 

with open('file/test.txt', 'w') as f1:
    f1.write("Hello, World!")
    f1.write('some\nfunny\ntext')

# with open('test3.py', 'r') as f2:
#     text = [line.strip() for line in f2.readlines().append('Hello, World!')]
#     for line in text:
#         print(line)


print(sys.argv)
print(sys.path)
print(sys.version) 
print(sys.platform)
print(sys.getfilesystemencoding())
