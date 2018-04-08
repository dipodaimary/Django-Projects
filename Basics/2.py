def my_fun(param1='default'):
    """
    THIS IS THE DOCSTRING
    """
    print("python function {}".format(param1))

my_fun()

def hello():
    return "Hello"

print(hello())

#function with inputs
def addNum(num1,num2):
    #check type
    if(type(num1)==type(num2)==type(10)):
        return num1+num2
    else:
        return "Sorry need integers"
print(addNum(2,3))

print(addNum('2','4'))

# Lamda expressions
#Filter
mylist = [1,2,3,4,5,6,7,8]
def even_bool(num):
    return num%2==0

evens = filter(even_bool,mylist)
print(list(evens))
#the lambda
evens = filter(lambda num:num%2==0,mylist)
print(list(evens))

#split
tweet = "Go sports! #Sports"
print(tweet.split('#'))

#in
print(3 in [1,2,3,4]);

#Exercies
print("Hello".endswith('lo'))
print("Hello"[-len("lo"):])
print("Hello"[-len("lo"):]=='lo')
