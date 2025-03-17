import sys 

with open('file/test.txt', 'w') as f1:
    f1.write("Hello, World!")
    f1.write('some\nfunny\ntext')

# with open('test3.py', 'r') as f2:
#     text = [line.strip() for line in f2.readlines().append('Hello, World!')]
#     for line in text:
#         print(line)


# print(sys.argv)
# print(sys.path)
# print(sys.version) 
# print(sys.platform)
# print(sys.getfilesystemencoding())

# def nice_function():
#     string = """Do nothing, but document it.
#     No, really, it doesn't do anything.
#     """    
#     return string
# def not_bad(s: str) -> str:
#     if s.find("not") == -1 or s.find("bad") == -1: 
#         print("not found")       
#         return s
#     else:
#         print("found")
#         return s.replace("not bad", "good")
# # s= "This music is not not bad"        
# #s = nice_function()
# print(not_bad(s))

