try:
    f = open('1.txt','r')
    f.write("this is a test file please delete is.")
except IOError:
    print("Error could not find file or read data")
else:
    print("Success")
    f.close()
finally:
    print("I always work no matter what")
print("Code continued to work")
