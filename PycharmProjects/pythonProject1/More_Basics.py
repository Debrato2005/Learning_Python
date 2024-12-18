#Using for loop with lists
pets=["cat","dog", "fish"]
for n,pet in enumerate(pets):
    print(f"{n+1}. {pet.title()} is a pet.")
print("DONE")
print()

for value in range(1, 6):
    print(value)
print()

for value in range(6):
    print(value)
print()

squares=[]
n=input("Enter number of squares u want to see:")
for value in range(1,int(n)+1):
    square=value**2
    squares.append(square)
print(squares)
print()

digits=[1,2,3,4,5,6,7]
print(min(digits))
print(max(digits))
print(sum(digits))
print()

#List Comprehensions
squares=[value**2 for value in range(1,11)]
print(squares)



