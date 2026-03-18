with open("demo","w+") as f:
   f.write("Hello world!\n")
   f.writelines("python ")
   f.seek(4)
   f.tell()
   print(f.tell())
   f.flush()
   temp1=f.read()
   print(temp1)
