#Lists 

L = ['Michael Jackson', 10.1,1982]
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )

#nesting 
list1 = ["Michael Jackson", 10.1, 1982, [1, 2], ("A", 1)]
print (list1[1])
print (list1[3])
print (list1[4])
print (list1[3:5])

#extend
list1.extend(['pop', 10])
print (list1)

#append 
list1.append(['jazz', 12])
print (list1)
list1[0] = "PINK"
print (list1)
del(list1[2])
print (list1)
