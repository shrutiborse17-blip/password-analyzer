import math 
import string

print("=====Advanced Password Security Analyzer")
password = input("enter the password ")

charset_size = 0 

if any(c.islower() for c in password):
  charset_size += 26 
if any(c.isupper() for c in password):
  charset_size += 26 
if any(c.isdigit() for c in password):
  charset_size += 10
if any(c in string.punctuation for c in password):
  charset_size += len(string.punctuation)

# calculate entropy 
entropy= len(password) * math.log2(charset_size) if charset_size else 0
entropy = round(entropy , 2)

#
if entropy < 28 :
  strength= "week"
elif entropy < 60 :
  strength= "medium"
else :
  strength = "strong"

print(f"password strenght : {strength}")
print(f"password entropy : {entropy} bits ")

