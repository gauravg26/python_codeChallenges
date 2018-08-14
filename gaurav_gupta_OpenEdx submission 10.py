
N = input("enter the num: ")

total = 0

for i in range(len(N)):
    if N[i]==13 or N[i-1]==13:
        continue
    total += N[i]

print total
