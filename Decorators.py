from functools import wraps
def decorator(mainfunc):
    @wraps(mainfunc)
    def wrapper():
        print("SOmething at Start")
        mainfunc()
        print("Something at End")
    return wrapper
@decorator
def mainfunc():
    print("This is the main function")

mainfunc()