"""Set are unordered, unchangeable, and do not allow duplicate values."""
a={'data','text','word','letter','sentence'}
print(a)

a={'data','text','word','letter','sentence',True,False,'text',1,0,2}
print(a)
print(len(a))
print(type(a))

for x in a:   
  print(x)        
print('text' in a)
print('text' not in a)

a.add('factor')
print(a)
