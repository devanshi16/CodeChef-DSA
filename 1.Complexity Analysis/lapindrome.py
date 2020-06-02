#Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome.
t = int(input(""))
def checking_lapindrome(n):
    length = len(n)//2
    n1 = n[:length]
    n2 = n[-length:]
    if sorted(n1)==sorted(n2):
        return True
    else:
        return False
for _ in range(t):
    n = input("")
    print("Yes" if checking_lapindrome(n) else "No") 