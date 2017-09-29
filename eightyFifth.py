import glob


def file_counter():
    List = glob.glob1("File_Counter", "*.py")
    print "There are %d python files" % len(List)


file_counter()
