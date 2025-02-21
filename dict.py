"""dict are ordered, changeable and do not allow duplicates"""

a={
  "city": "Paris",
  "country": "France",
  "population": 2148000
}
print(a)
print(len(a))
print(a["city"])

x = a.keys()
print(x)           #before the change
a["people"] = "white people"
print(x)           #after the change

x = a.values()
print(x)           
a["population"] = "2228000"
print(x)

a.pop("people")
print(a)