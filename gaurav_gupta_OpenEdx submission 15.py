
for num in range(50):
    if num % 5 == 0 and num % 3 == 0:
        print("fizzbuzz")
        continue
    elif num % 3 == 0:
        print ("fizz")
        continue
    elif num % 5 == 0:
        print ("buzz")
        continue
    else:
        print (num)
