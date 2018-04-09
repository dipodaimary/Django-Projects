def fun():
    mylocal = 1
    print(locals())
    print(globals())
    return 1

print(fun())

#
def hello(name="Jose"):
    return ("hello "+name)

mynewgreet = hello

print(mynewgreet())
