import random
with open("demo","w+") as f:
    for i in range(20):
       n=random.randint(1,100)
       f.write(str(n)+"\n")
print("20 random numbers inserted")
