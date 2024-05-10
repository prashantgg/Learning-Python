with open ("donkey.txt", "r") as f:
   read = f.read()
   print (read)


   rep = read.replace ("Donkey", "######")
   with open ("donkey.txt", "w") as f:
       f.write(rep)
  


   