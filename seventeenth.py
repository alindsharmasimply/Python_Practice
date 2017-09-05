# Reading files
file = open("C:\\Users\\S K Sharma\\Downloads\\testForPython.txt","r")
print "The name of the file is", file.name
print "The mode is", file.mode
print "The file is closed ??", file.closed
file.close()
print "The file is closed", file.closed

#Writing files
file = open("C:\\Users\\S K Sharma\\Desktop\\write_test.txt","w+")
file.write("Hey! I am a new file. ")
file.write("I'm new to this computer.")
file.seek(0)
print file.read()
file.close()