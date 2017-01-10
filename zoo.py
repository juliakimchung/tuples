zoo = tuple()
zoo = ("panda", "polor-bear", "fox", "bird", "tiger", "elephant")
value = zoo.index("polor-bear")
print(value * 3)
zoo.index("fox")
print(zoo.index("fox"))
 
print("panda" in zoo)

for x in zoo:
	print(x)

print(zoo[0:5:2])
I = list(zoo)
print(I)
I.extend(["monkey", "red-panda", "ant-eater"])
print(I)
I = tuple(I)
print(I)
