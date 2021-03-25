fname = "/home/pi/Documents/Other files/MORG.log"
count = 0
with open(fname, 'r') as f:
    for line in f:
        count += 1
print("Total number of lines is:", count)

a_file = open(fname, "r")


lines = a_file.readlines()
a_file.close()

del lines[5]
del lines[6]
del lines[7]
del lines[8]
del lines[9]
del lines[10]


new_file = open("/home/pi/Documents/Other files/MORG.log", "w+")

for line in lines:
    new_file.write(line)

new_file.close()