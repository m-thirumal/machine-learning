name=["Thirumal", "Angelina", "Kate", "Jessica"]
id=[1, 2, 3, 4]
mapped = zip(name, id)
print("Zip: ", mapped)
#conver to set
mapped = set(mapped)
print("After converting to set: ", mapped)

for n, i in zip(name, id):
    print("Name %s & id %d" %(n, i))

#Unzip
name, id = zip(*mapped)
print("Unziped name: ", name)
print("Unziped id: ", id)