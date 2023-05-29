string="segmetriq analytics"
vowels=['a','e','i','o','u','A','E','I','O','U']
res=""
for i in range(len(string)):
    if string(i) not in vowels:
        res=res+string(i)
print("\n find owels in this list",res)
