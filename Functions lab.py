#Functions lab 
def add(a):
    b=a+1
    print (a,"if add one",b)
    return(b) 
add(1)
add(34)

#new function
def mult(a,b):
    c = a * b
    print (c)
    return(c)

mult(24,3)
mult (19.3,29.74)
mult (3, "buy")

#new function
def square (a):
    b = 1 
    c = a*a+b
    print(a, "if you square + 1", c) 
    return(c)
square (23)

#one more 
def com(a,b):
    return(a+b)

print (com(8,5))
print (com("This ", "is"))

#pre-defined functions

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 

print (album_ratings)
print (sum(album_ratings))
print (len(album_ratings))

def albumtype (artist, album, year):
    print (artist, album, year)
    if year > 1980:
        return "Modern"
    else: 
        return "Old"
    
y = albumtype ("Sher", "Name i dont know", 1978)
print (y)

y = albumtype ("Pumpkin", "Bla bla ", 1998)

#loop in function 
def PrintList(the_list):
    for element in the_list:
        print(element)
PrintList(['1', 1, 'the man', "abc"])

#matching string 

def match (x,y):
    if x==y:
        return 1
    
string1 = "Mememe"
string2 = "Mememe"  
check = match(string1, string2)
string2 = "Mememe"  
if check == 1:
    print ("Match")
else:
    print ("No match")

# Python Program to Count words in a String using Dictionary

def freq(string):
    word = []
    word = string.split ()
    dict = {}

    for key in word:
        dict[key]=word.count(key)
        print("The Frequency of words is:",dict)

freq ("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")


def isGoodRating(rating=4): 
    if(rating < 7):
        print("this album sucks it's rating is",rating)
        
    else:
        print("this album is good its rating is",rating)

isGoodRating(10)

def devide (a,b):
    c=a/b
    print (c)
    return (c)

devide (6,2)


