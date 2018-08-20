# addition function
def add(*args):
    print args
    addition = 0
    for item in args:
        addition += item
    return addition
# Multiplication function
def mul(*args):
    multiply = 1
    for item in args:
        multiply = multiply* item
    return multiply
# Largest number Function
def lar(*args):
    largest = 0
    for item in args:
        if item > largest:
            largest=item
    return largest
# Smallest number Function
def small(*args):
    smallest = args
    for item in args:
        if item < smallest:
            smallest = item
    return smallest
#sorting function
def sort(*args):
    x = sorted(args)
    return x
# Remove_Dublicates
def no_dub(*args):
    z = set(args)
    return list(z)
#Result
print "sum = " + str(add(1,2,3,4,5))
print "multiply = " + str(mul(1,2,3,4,5))
print "largest number = " + str(lar(5,546,4,694,64,61,6))
print "smallest number =" + str(small(596,41,646,319,432,46,265))
print "sorting = " + str(sort(65,494,94,46,64,6,2))
print "no dublicate = " + str(no_dub(49,496,46,64,56,49,64,44))