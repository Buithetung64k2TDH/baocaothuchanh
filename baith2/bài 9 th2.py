input("Bui The Tung  MSV 235752021610074")
str=input("Enter a string: ")
dict = {}
for n in str:
    keys = dict.keys()
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print (dict)
