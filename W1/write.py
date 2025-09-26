# Generate the string
a = "A" * 100000
b = "B" * 100000
c = "C" * 100000
s = a + b + c


# Write to file
with open("VERY-LONG.txt", "w") as f:
    f.write(s)