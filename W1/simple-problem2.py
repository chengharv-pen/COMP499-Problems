# Read input
N = int(input())

# Calculate sum of first N natural numbers
s = N * (N + 1) // 2

# Check if sum is odd
if s % 2 == 1:
    print("NO")
    exit()

print("YES")

# Target sum is half of total sum
s = s // 2

# Find numbers to reach target sum
i = N
temp_sum = 0

while i + temp_sum <= s:
    temp_sum += i
    i -= 1

# When loop stops, i is on the number that would exceed the sum
missing_number = s - temp_sum

# Print first set: numbers from i+1 to N plus missing_number
print(N - i + 1)
print(*range(i + 1, N + 1), missing_number)

# Print second set: numbers from 1 to i excluding missing_number
print(i)
for j in range(1, i + 1):
    if j != missing_number:
        print(j, end=" ")