def password_checker():
    p = raw_input("Enter a password ")
    if any(i.isdigit() for i in p) and any(i.isupper() for i in p) and len(p) >= 5:
        print "Your password is OK "

    else:
        print "Your password is not fine "


password_checker()
