# Generate the string
s = "ABC" * 100000  # length = 300,000

# Then shuffle if needed, e.g.:
import random
s = list(s)
random.shuffle(s)
s = ''.join(s)

# Write to file
with open("input.txt", "w") as f:
    f.write(s)