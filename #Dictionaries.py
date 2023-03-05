#Dictionaries
d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
new = (d["India"])
print(new)


d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
new = d["India"] = 'Rs'
print(new)
print(d)

d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
new = d["Japan"] = 'Yen'
print(new)
print(d)

d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
del d["India"]
print(d)

d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
new = sorted(d)
print(new)
print(d)

d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
new = d.values()
print(new)
print(d)

d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
new = d.keys()
print(new)
print(d)

d = {"India" : "INR", "USA" : "USD", "France" : "Euros"}
new = d.update({'India':'Rupee'})
print(new)
print(d)