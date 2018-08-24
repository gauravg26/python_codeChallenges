

def translate(s):
    consonants = 'bcdfghjklmnpqrstvwx'
    lst = []
    for i in s:
        if i not in consonants:
            lst.append(i)
        else:
            lst.append(i)
            lst.append("o")
            lst.append(i)  
    print ''.join(lst)


translate (raw_input("write the text: "))
