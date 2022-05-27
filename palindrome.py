
def palindrome(name):
    if (name==name[-1::-1]):
        return True
    return False
a=input("Enter a word  ")
print(palindrome(a))
