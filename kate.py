# data = 1.05 * 0.8 * (5.67 * 0.00000001)
# dataTwo = (950 * 950 * 950 * 950) - (962 * 962)
# dataThree

a = 0.85
b = 1.1
h = 0.5
side = h * a
back = h * b
floor = a * b

s = (side * 2) + (floor * 2) + back
print("S = ",s)

# second part

data = 1.05 * 0.8 * (5.67 * 0.00000001)
dataTwo = ((1000 * 1000 * 1000 * 1000) - (962 * 962 * 962 * 962)) / (1000 - 962)
dataThree = data * dataTwo
print(dataThree)

