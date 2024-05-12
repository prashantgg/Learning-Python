class Att:
    a = 5

obj = Att()
obj.a = 0

print (Att.a)
print (obj.a)
  

# No the class attribute does not changes when an object attribute is created
#For changing class attribute this can be done
# Att.a = 8
# print (Att.a)