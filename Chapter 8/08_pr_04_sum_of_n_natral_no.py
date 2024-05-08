def sum(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
      return sum(num-1) + num

num = 10
print ("Sum is: ", sum(num))

