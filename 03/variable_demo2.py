#Create a global variable, outside if a function
glb_var = "global"

#Define a function
def var_function():
    lcl_var = "local" 
    #Creating a local variable inside a function
    print(lcl_var)
    print(glb_var) #Print global variable within the function

#Call function to print local variable 
var_function()

#Print global variable outside function
print(glb_var)


