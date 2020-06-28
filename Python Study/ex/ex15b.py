from sys import argv

script, filename = argv
print(type(filename))
print(script)
print(filename)
with open(filename) as f:
    print(f.read())
print("success!")

