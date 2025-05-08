# RANDOM PASSWORD GENERATOR

import random
import string
#print(string.ascii_letters)     #prints all small and capital letters
val=string.ascii_letters + string.digits + string.punctuation
random.choice(val)
pass_len=12
password=""
for i in range(pass_len):            #or instead of from line 9 to 11 we can type as  res="".join([random.choice(val) for i in range(pass_len)])
     password+=random.choice(val)     #  print(res)
    
print("The randomly generated password is:", password)    