
my_dict = {'a':13,'b':15,'c':16}
s = my_dict.values()
total = 0
for i in range(len(s)):
    if s[i]==13 or s[i]==14 or s[i]==17 or s[i] ==18 or s[i]==19:
        continue
    total += s[i]

print total
