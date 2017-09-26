

def advanced_password_checker():
    p = raw_input("Enter your password ")
    L = []
    if len(p) < 5:
        L.append("You need to have a length of atleast 5 characters.")
    if not any(i.isupper() for i in p):
        L.append("You need atleast one upper case character.")
    if not any(i.isdigit() for i in p):
        L.append("You need atleast one digit.")
    if len(L) == 0:
        print "Your password is fine."
    else:
        print L


advanced_password_checker()
