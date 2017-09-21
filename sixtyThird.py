input_file = raw_input("Enter the file name to be edited ")

output_file = raw_input("Enter the output file name ")


fp1 = open(input_file, "r")

fp2 = open(output_file, "a")
x = 0
for i in fp1:
	rd = fp1.readline(i)
	fp2.write(str(x+1),": ",rd)

fp1.close()
fp2.close()