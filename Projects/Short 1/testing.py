line = input("gimme name n age: ")

name, age = ' '.join(line.split()[:-1]), line.split()[-1]

print(name)
print(age)
