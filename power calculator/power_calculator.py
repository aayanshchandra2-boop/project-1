base = int(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
result = base ** exponent
print(f"{base} raised to the power of {exponent} is {result}")
result = base ** exponent
for i in range(1, exponent + 1):
   result = result * base
   print("step", i, ":", result)

print("\nAnswer:", base , "to the power of", exponent, "is", result)
