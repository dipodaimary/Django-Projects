import one
print("TOP LEVEL TWO.PY")
one.func()
if __name__=='__main__':
    print('Tow.py is being run directly')
else:
    print('two.py is being imported')
