#Q.1- Write a python code to find a valid email address from a text.
import re
id=input('Enter Email-ID:')
match=re.fullmatch('^[a-zA-Z][_a-zA-z0-9.]*(@)(gmail.com|yahoo.com)',id)
if match:
    print(id,'IS VALID')
else:
    print(id,'IS NOT VALID')
  
'''
Q.2- Write a python program to find a valid Indian phone number from a text.
(Valid Indian numbers will start with "+91-" and after that [6-9] followed by 9 digits. )
'''
import re
num=input('Enter Indian Phone number:')

match=re.fullmatch('(\+91-)[6-9]\d{9}',num)
if match:
    print(num,'IS VALID')
else:
    print(num,'IS NOT VALID')
