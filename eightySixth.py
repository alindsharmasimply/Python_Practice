import glob


def recursive_finder():
    List = glob.glob("subdirs/**/*.py")
    print "Number of files are ", len(List)


recursive_finder()
