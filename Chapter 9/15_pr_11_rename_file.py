import os
with open ("copy.txt") as f:            
    read = f.read()


with open ("removed_by_python.txt", "w") as f:
    f.write(read)


os.remove ("copy.txt")