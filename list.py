"""List items are ordered, changeable, and allow duplicate values."""

list=['data','text','word','letter','sentence']
print(list)               

"""Duplicates"""
list=['data','text','word','letter','text','sentence']
print(list)               

"""length of the list"""
list=['data','text','word','letter','sentence']
print(len(list))        
print(type(list))                    

"""indexing"""
print(list[1])            

"""Negative Indexing"""
print(list[-3])           

"""Range of Indexes"""
print(list[1:5])          

print(list[-4:-1])        

"""change value"""
list[1:3] = ["number", "factor"]
print(list)               

"""insertion"""
list.insert(2,'text')
print(list)               

"""append"""
list.append('word')
print(list)               

"""remove"""
list.remove('word')
print(list)               

list.pop(1)               #If you do not specify the index, the pop() method removes the last item.
print(list)               
del list[1]
print(list)               

list=['data','text','word','letter','sentence']
print(list)

"""sorting"""
list.sort()               #sort() method that will sort the list alphanumerically, ascending, by default.
print(list)             
