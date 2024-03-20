'''
^ -1 st condition
[] - range
+ - merging conditions
\ - character search sring
? - 1 se zyada nahi hona chahiye 
\w - searches that string
{} - search on that position with "$" sign
'''
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("ENTER YOUR MAILD ID : ")
if re.search(email_condition,user_email):
    print("RIGHT EMAIL")
else:
    print("WRONG EMAIL")    