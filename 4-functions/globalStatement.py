# If you need to modify a global variable from within a function, use the global statement. Including a line such as global eggs at the top of a function tells Python, “In this function, eggs refers to the global variable, so don’t create a local variable with this name.”
def spam():
   global eggs
   eggs = 'spam'

eggs = 'global'
spam()
print(eggs)  # Prints 'spam'