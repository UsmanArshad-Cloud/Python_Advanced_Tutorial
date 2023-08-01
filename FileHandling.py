"""
    Modes in Python
    'r'->open the file for read only and gives an error if the file is not present(Defualt)
    'w'->opens the file for writing only and creates the new file if the file does not exist overwrite the existing content
    'a'->opens the file for append only and creates the new file if the file does not exist
    'x'->creates the file gives error if already exist
    To close a file you can use f.close() so that resources can be freed
    Alternatively you can use with statement.It will automatically close the file
    seek(10)->move the current position within a file to a specified point
    read(5)->read is used to read from the file if some number is specified then it means read 5 characters
    tell()->is used to find the current position withing the file.
"""
f = open('myfile.txt', 'r')
#text = f.read()
#print(text)
while True:
    line = f.readline()
    if not line:
        break
with open('myfile2.txt', 'a') as f:
    f.write("Hello")

f=open('myfile.txt','w')
lines=["1\n","2\n","3\n"]
f.writelines(lines)
f.close()
