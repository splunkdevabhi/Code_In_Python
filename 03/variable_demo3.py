#Create a global variable, outside if a function
glb_var = "global"

#Define a function
def var_function():
    lcl_var = "local" 
    #Creating a local variable inside a function
    print(lcl_var)

#Call function to print local variable 
var_function()

#Print global variable outside function
print(lcl_var)


