import random 
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "1234567890"
Symbol = "!@#$%^&*"

all = lower + upper + NUMBER + Symbol
length = 6
password = "".join(random.sample(all,length))
print("The randomised Password You Generated is :",password)