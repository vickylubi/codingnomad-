#equal: ==
#not equal: !=
#greater than: >
#less than: <
#greater than or equal to: >=
#less than or equal to: <=

# Condition Equal
a = 6 
print (a== 56)
print (a==6)
print ("--------")
print ("me"=="you")
print ("me"!="you")
print ("--------")
print ("A"> "B")
print ("--------")
age = 18 
if age > 19:
    print ("You can enter")
else:
    print ("No enter")
print ("Next!")

print ("--------")
age = 18 
if age > 19:
    print ("You can enter")
elif age == 18:
    print ("Wait")
else:
    print ("No enter")
print ("Next!")
print ("--------")
# Condition statement example
relise = 1995
if relise > 1990 and relise < 2000:
    print ("its within the limit")
else: 
    print ("not okay")
# Condition statement example
print ("--------")
relise = 3000
if relise > 1990 or relise < 2000:
    print ("its within the limit")
else: 
    print ("not okay")
print ("--------")
#not statement 
date = 1993
if not (date == 1997):
    print ("it is not 1997")
