i = -1
reverse = ''


def palindrome(s):
    global i
    if i < -len(s):
        return
    global reverse
    n = s[i]
    i -= 1
    reverse = reverse + n
    palindrome(s)


def main():
    s = raw_input("Enter a string ")
    palindrome(s)
    if s == reverse:
        print "The string is palindrome"
    else:
        print "The string is not a palindrome"


main()
