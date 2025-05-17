def uppercase(func):
    def wrapper(*args, **kwargs):
        print("uppercase: vor Funktionsaufruf")
        result = func(*args, **kwargs)
        print("uppercase: nach Funktionsaufruf")
        return result.upper()

    return wrapper


def exclaim(func):
    def wrapper(*args, **kwargs):
        print("exclaim: vor Funktionsaufruf")
        result = func(*args, **kwargs)
        print("exclaim: nach Funktionsaufruf")
        return result + "!"

    return wrapper


def greet():
    print("greet wird ausgeführt")
    return "hello"


greets = uppercase(exclaim(greet))
print("stop mal")
a = greets()
print(a)
