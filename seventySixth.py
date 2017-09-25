import webbrowser

g = raw_input("Enter your google query")
URL = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q=%s" % g
webbrowser.open_new(URL)
