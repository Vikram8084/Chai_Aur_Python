# default parameter values
# write a function that greets a user .if no name is proivided,it should greet with a default name.

def greet(name ="User"):
    return "Hello, " + name + " ! "

print(greet("chai"))
print(greet())