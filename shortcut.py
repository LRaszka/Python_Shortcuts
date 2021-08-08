# F Strings
name = "Lukas"
print(f'Hello {name} {[1,2,3]} {1}')

# Unpacking
tup = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
string = "hello"
dic = {"a": 1, "b": 2}
coords = [4, 5]

a, b, c, d, e = tup
print(a, b, c, d, e)
a, b, c, d, e = lst
print(a, b, c, d, e)
a, b, c, d, e = string
print(a, b, c, d, e)
a, b = dic
print(a, b)
a, b = dic.values()
print(a, b)
a, b = dic.items()
print(a, b)
a, b = coords
print(a, b)

# Multiple Assignment
width, height = 400, 500
width, height = height, width
print(width, height)
width, height, x = height, width, 5
print(width, height)

# Comprehensions
x = [0 for i in range(100)]
print(x)
x = [i for i in range(100) for j in range(10)]
print(x)
x = [[0 for _ in range(5)] for _ in range (5)]
print(x)
x = (i for i in "hello")
print(list(x))
sentence = "hello my name is lukas"
x = {char: sentence.count(char) for char in set (sentence)}
print(x)

# Object Multipliations
x = "hello" * 5
print(x)
x = [1, 2, 3, 4, 5] *5
print(x)
x = [[1, 2, 3]] * 5
print(x)
x = (1, 2) * 10
print(x)

# Inline/Ternary Condition
x = 1 if 2 > 3 else 0
print(x)

# Zip
names = ['tim', 'jose', 'billy', 'sally']
ages = [21, 18, 78, 45]
eye_color = ['blue', 'brown', 'green', 'blue']
print(list(zip(names, ages, eye_color)))
print(list(zip(names, ages)))
for name, age in zip(names, ages):
    if age > 20:
        print(name)

# *args and **kvargs
def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)

def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)
args = [2, 2, 3]
kwargs = {"arg2":2, "arg1": 1, "arg3": 3}

func1(*args)
print(*args)
func2(**kwargs)

# For else & While else
search = [1, 2, 3, 5, 6, 7]
target = 7

for element in search:
    if element == target:
        print('I found it!')
        break
else:
    print("I didn't find it")

i = 0
while i < len(search):
    element = search[i]
    if element == target:
        print('I found it!')
        break
    i += 1
else:
    print("I didn't find it")

# Sort by key
lst = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]
lst.sort()
print(lst)
lst.sort(key=lambda x: x[1])
print(lst)
def sort_func(x):
    return x[0] + x[1]
lst.sort(key=sort_func)
print(lst)

# Intertools
import itertools

lst = [1, 2, 3, 4, 5]
sum_list = itertools.accumulate(lst)
print(list(sum_list))

names = ['tim', 'jose', 'billy', 'sally', 'Jen']
show = [1, 0, 1, 1, 0]
compressed_list = itertools.compress(names, show)
print(list(compressed_list))