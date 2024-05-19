def filt(num):
    if num%5 == 0:
        return True
    else:
        return False

l1 = [1,5,6,10,20,24,29,30,25,26,40,49,50]
a = list(filter(filt, l1))
print (a)