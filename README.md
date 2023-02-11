# Python-scope
A variable in only available from inside the region it is creaed. This is called scope.

# Local Scope
A variable created inside a function belongs to the local scope of that function, add can only be used inside that function.

# Example
A variable created inside a function is available inside that function:

    def myfunc():
        x = 300
        print(x)

    myfunc()


# Function Inside Function
As explained in the example above, the varaible x is not availabe not outside the function, but it is a availble for any function inside the function:

# Example
The local varaible can be accessed from a function within the function:

    def myfunc():
        x = 300
        def myinnerfunc():
            print(x)

        myinnerfunc()

    myfunc()        

# Global Scope 
A varaible created in the main body of the Python code is a global varaible and belongs to the global scope. 

Global variables are available from within any scope, global and local.

# Example
A variable created outside of a function is global and can be used by anyone:

    x = 300

    def myfunc():
        print(x)

    myfunc()    
    print(x)

# Naming Variables 
If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one availabe in the global scope(outside the function) and one available in the local scope( inside the function):

# Example
The function will print the local x, and then the code will print the global x:

    x = 300
    
    def myfunc():
        x = 200
        print(x)

    myfunc()

    print(x)    


