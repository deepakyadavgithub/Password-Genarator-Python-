import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "1234567890"
Symbol = "!@#$%^&*"
a="yes"
while a="yes":
  all = lower + upper + NUMBER + Symbol #this helps to make a strong password  because strorng password is a sum of  all special character
 
  length = 6
  password = "".join(random.sample(all,length))
  print("The randomised Password You Generated is :",password)
  a=input("do you want to generate more yes/no" :)
  if a=="no":
    break
