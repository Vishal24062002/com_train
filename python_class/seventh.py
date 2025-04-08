# f=open('demo.txt','r')
# # print(f.read())
# # print(f.read(10))  # 10 strands for how many char to print
# # print(f.readline()) #it print first line
# # print(f.readline()) # and it print 2 line

# print(f.readlines()) # it print all the lines in list format



# f.close()

# writing a file

# f=open('demo1.txt','w') # it will create new file in write mode and does not create in read mode
# f.write("java\n")  # if we write before this again we write new in same file and run it will be overwrite 
# f.write("py world\n")
# f=open('demo1.txt','w')


# f.writelines(['hello woreld \n','hello py\n']) 

# f=open('demo1.txt','a+') # a stand for append it also create a new file 
# f.write("py hi\n")
# print(f.tell())
# f.write("py buy\n")
# f.seek(0)
# print(f.read()) 

# f.close()

# with open('demo.txt','r') as f:
#     print(f.read())
    
# print(f.closed)

with open('demo.txt','r') as f:
    with open('demo.txt','r') as f:
        print(f.read())
    

    
print(f.closed)
