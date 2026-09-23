number = int(input("Enter a number: "))
print(f"Times Table for {number} (1 to 10):")
for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")
