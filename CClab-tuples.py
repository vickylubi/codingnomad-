# artist - Name of the artist
# album - Name of the album
# released_year - Year the album was released
# length_min_sec - Length of the album (hours,minutes,seconds)
# genre - Genre of the album
# music_recording_sales_millions - Music recording sales (millions in USD) on SONG://DATABASE
# claimed_sales_millions - Album's claimed sales (millions in USD) on SONG://DATABASE
# date_released - Date on which the album was released
# soundtrack - Indicates if the album is the movie soundtrack (Y) or (N)
# rating_of_friends - Indicates the rating from your friends from 1 to 10

# Create your first tuple
tuple1 = ('disco',10,1.2)
# Print the type of the tuple you created
type(tuple1)
# Print the variable on each index
print(tuple1[0])
print(tuple1[1])
print(tuple1[2])
# Print the type of value on each index
print(type(tuple1[0]))
print(type(tuple1[1]))
print (type(tuple1[2]))
# Use negative index to get the value of the last element
print(tuple1[-1])
# Concatenate two tuples
tuple2 = tuple1 + ('hard rock',10)
print (tuple2)
# Slice from index 0 to index 2
print (tuple2[0:3])
# Slice from index 3 to index 4
print(tuple2[3:4])
# Get the length of tuple
print(len(tuple2))
# A sample tuple
ratings = (0,9,6,5,10,8,9,6,2)
print (ratings)
# Sort the tuple
ratings_sorted = sorted(ratings)
print (ratings_sorted)
# Create a nest tuple
nested_tuple = (1,2,('pop','rock'),(3,4),('disco',(1,2)))
# Print element on each index
print ("0 Element of the tuple: ", nested_tuple[0])
print ("1 Element of the tuple: ", nested_tuple[1])
print ("2 Element of the tuple: ", nested_tuple[2])
print ("3 Element of the tuple: ", nested_tuple[3])
print ("4 Element of the tuple: ", nested_tuple[4])
# Print element on each index, including nest indexes
print ("2.0 Element of the tuple: ", nested_tuple[2][0])
print ("2.1 Element of the tuple: ", nested_tuple[2][1])
print (nested_tuple[2][1][1])
print (nested_tuple[4][1][0])
print (nested_tuple[4][1][1])
# sample tuple
genres_tuple = ("pop", "rock", "soul", "hard rock", "soft rock", "R&B", "progressive rock", "disco") 
print(len(genres_tuple))
print (genres_tuple[3])
print(genres_tuple[3:6])
print (genres_tuple[0:2])
print(genres_tuple[-1][0])
c_tuple = (-5,1,-3)
sorted_c_tuple = sorted (c_tuple)
print (sorted_c_tuple)
















