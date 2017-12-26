s=input("Enter a string: ")
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
d1 = {letter: 0 for letter in alphabets}
 for ch in s:
        d1[ch] += 1
        for key in d1:
             print(key,d1[key])

