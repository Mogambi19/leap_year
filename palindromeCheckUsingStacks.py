import re #import the regular expressions module
def palindromeCheckUsingStacks(string)->bool:
    stack = []
    for character in string:
        stack.append(character)
    reversedString = ""
    while len(stack)!=0:
        reversedString+=stack.pop()
    if string==reversedString:
        print("This string is a palindrome")
        return True
    else:
        print("This string is not a palindrome")
        return False

userInput = input("Enter the string you want to test:")
cleanedUserInput = re.sub(r'[^a-z]','',userInput.lower())#remover everything except lower case letters
palindromeCheckUsingStacks(cleanedUserInput)
