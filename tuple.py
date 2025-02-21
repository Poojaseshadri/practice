"""A tuple is a collection which is ordered and unchangeable."""
tuple=('data','text','word','letter','sentence')
print(tuple)  

"""Duplicates"""
tuple=('data','text','word','letter','text','sentence')
print(tuple)  

"""Length"""
tuple=('data','text','word','letter','text','sentence')
print(len(tuple))  

"""class type"""
tuple=('data','text','word','letter','text','sentence')
print(type(tuple))  

"""constructor"""
tuple=(('data','text','word','letter','text','sentence'))
print(tuple)

"""Indexing"""
tuple=('data','text','word','letter','text','sentence')
print(tuple[1:])
print(tuple[-5:-1])

a=('data','text','word','letter','sentence')
b=list(a)
b[1]="factor"
c=tuple(b)
print(c)