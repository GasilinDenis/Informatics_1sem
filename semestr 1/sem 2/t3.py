mirror = {
    'A': 'A', 'H': 'H', 'I': 'I', 'M': 'M', 'O': 'O', 'T': 'T', 'U': 'U',
    'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', '1': '1', '8': '8',
    'E': '3', 'J': 'L', 'S': '2', 'Z': '5', '3': 'E', 'L': 'J', '2': 'S', '5': 'Z'
}
s = input().strip()
m=0
p=0
mirs=str()
if s == s[::-1]:
    p=1
for i in s:
    if i not in mirror: break
    mirs += mirror[i]

if s == mirs[::-1]:
    m=1

if m==1 and p==1:
    print(s, 'mirrored palindrome ')
elif m==1: print(s, 'is a mirrored string')
elif p==1: print(s, 'is a regular palindrome')
else: print (s, 'is not a palindrome')