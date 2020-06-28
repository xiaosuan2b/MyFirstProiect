#this one is like your scripts with argv
def print_two(*args):
    arg1,arg2 = args
    print(f"arg1:{arg1},\narg2:{arg2}")

#ok,that *args is actually pointless ,we can just do this
def print_two_arain(arg1,arg2):
    print(f"arg1:{arg1},\narg2:{arg2}")

def print_one(arg1):
    print(f"arg1:{arg1}")
    
#this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("xiaosuan","2b")
print_two_arain("Xiaosuan","2b")
print_one("Nb!")
print_none()