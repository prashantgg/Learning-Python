def remove_strip (string, word):
    a = string.replace (word, " ")
    return a.strip()



this = "      Harry is a good       "
print (remove_strip(this, "Harry"))





# print(this)
# print (this.strip())
