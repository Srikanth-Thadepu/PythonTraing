import array
l1=[]
print("1. An empty list",l1)

l2=[1,2,3,4]
print("2. List with four elements: ",l2)

l3=['abc',['def','ghi']]
print("3. Nested list: ",l3)

l4=list('spam')
print("4. List created from string 'spam': ")

l5=list(range(-4,4))
print("5. List created from range(-4,4): ")

l6=[12,23,34,45]
print("6. Element at index 2: ",l6[2])

l7=['i',[10,20,30],'j'] #accessing an element in nested list through index
print("7. Element at l7[1][2] nested list: ",l7[1][2])

l8=[0,1,2,3,4,5]
print("8. Slicing l8 from index 2 to 4: ",l8[2:5])

l9=[10,[100,200,300,400],20]
print("9a. Element at l9[1]: ",l9[1]) #access the sublist
print("9b. Element at l9[1][3]: ",l9[1][9])
print("9c. Slicing sublist l9[1][1:3]: ",l9[1][1:3])