# Testing environment
import math
from Test2 import test_var
var = test_var
test_array = [0, 1, 2, 3]


def testing_function(one, two, three, four):
    print(one, "one")
    print(two, "2")
    print(three, "drie")
    print(four, "quatre")


# testing_function(*test_array)

print(math.sin(0.5 * math.pi))


def testing():
    global var
    for n in range(5):
        var += 1
        print("this works")


testing()
print(var)
