#range object 

print (range(5))

#for loops 
dates = [1991, 1971, 1970]
N = len(dates)
for i in range(N):
    print (dates[i])

# Example of for loop
for i in range (8):
    print (i)

# Example of for loop, loop through list
date = [1551, 1832, 1093]
for year in date:  
    print(year)  

# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range (5):
    print ("Before color", i, "is", squares[i])
    squares [i] = "white"
    print ("After color", i, "is", squares [i])

    # Loop through the list and iterate on both index and element value
    things = ["phone", "cup", "notebook", "pen"]
    for i, elephant in enumerate(things):
        print (i,elephant)

    #While loops 
    print ("------------------- While Loops --------------------")

    count = 1

    while count <= 5:
        print (count)
        count += 1

# While Loop Example

dates = [1982, 1980, 1973, 2000]
i = 0 
year = dates[0]

while (year != 1973):
    print (year)
    i = i + 1
    year = dates[i]
    print("It took ", i ,"repetitions to get out of loop.")

print ('-----------------Test1--------------------')
#Write a for loop the prints out all the element between -5 and 5 using the range function.
for a in range (-5,6):
    print (a)
print ('-----------------Test2--------------------')
#Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for i in range (0,6):
    print (genres[i])

Genres = ['rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for Genre in Genres:
    print(Genre)

print ('-----------------Test3--------------------')
#Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']
squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares: 
    print (square)

print ('-----------------Test4--------------------')
#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
# If the score is less than 6, exit the loop. The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]

while i < len (PlayListRatings) and rating > 6:
    print (rating)
    i += 1
    rating = PlayListRatings[i]


#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
# Stop and exit the loop if the value on the list is not 'orange'

squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
new_squares = []
i = 0

while (i < len (squares) and squares [i] == 'orange'):
    new_squares.append (squares[i])
    i += 1
    print (new_squares)



