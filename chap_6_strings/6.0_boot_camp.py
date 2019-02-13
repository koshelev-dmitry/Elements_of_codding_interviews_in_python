def ispalindromic(s):
    generat = (s[i] == s[~i] for i in range(len(s)//2))
    print(generat)
    print(next(generat))
    return all(generat)

# print(ispalindromic("aaaaaaaaaaaaaaaaaaaaaa"))
s = "abcaaaa"
print(s.startswith("ac"))