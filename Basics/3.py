x =25
def my_fun():
    x=50
    return x

print(x)
my_fun()
print(x)

#to change global variable not recommeneded unless you have to
def func2():
    global x
    x = 1000

func2()
print(x)
