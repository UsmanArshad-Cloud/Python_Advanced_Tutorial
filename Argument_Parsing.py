# *args and **kwargs
import sys

print(f"Hello+{sys.argv[0]}")
filename = sys.argv[1]
message = sys.argv[2]
with open(filename,'w+') as f:
    f.write(message)


def myfunction(*args, **kwargs):
    print("Arguments in Args")
    for item in args:
        print(item)
    print("Arguments in Kwargs")
    for key, value in kwargs.items():
        print(f"Key is {key} and value is {value}")


arg = ["1", "2", "3"]
kwarg = {"Name": "Usman", "FName": "Arshad"}

myfunction("Hello", 1, 2, 3, True, Nice="Nice", good="Good", *arg, **kwarg)
