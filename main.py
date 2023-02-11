#Local Scope 
def myfunc():
    x = 300
    print(x)

myfunc()

#! Or 

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()     


#Global Scope
x = 300

def myfunc():
    print(x)
myfunc()  
print(x)


#Naming Variables
x = 900

def myfunc():
    x = 200
    print(x)
myfunc()
print(x)    


#Global Keyword
def myfunc():
    global x
    x = 1500

myfunc()
print(x)

# ! Or

x = 3000
def myfunc():
    global x
    x = 200

myfunc()
print(x)    
#To change the value of a globa variable inside a function, refer to the varaible by using the global keyword.