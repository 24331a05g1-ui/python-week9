with open("demo","w+") as f:
   f.write("Hello world!\n")
   f.writelines("python lab")
with open("demo","r") as f:
   temp2=f.readlines(2)
   print(temp2)
   temp=f.read()
   print(temp)
   f.seek(0)
   temp1=f.readline(5)
   print(temp1)
