word = ["mote", "hatti", "donkey", "chor", "gaida"]

with open ("donkey.txt", "r") as f:
   read = f.read()


for words in word:
   read = read.replace (words, "######")
   with open ("donkey.txt", "w") as f:
       f.write(read)



  

   