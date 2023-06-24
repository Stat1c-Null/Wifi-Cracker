import itertools as its
words = "1234567890abcdefghijklmnopqrstuvwxyz" # a set of password characters
r =its.product(words,repeat=8)  # random combination of 8 characters
dic = open("pwd.txt","a")      # creates a new pwd.txt file and store random wifi combinations in file
for i in r:
    dic.write("".join(i))
    dic.write("".join("\n"))
dic.close()
