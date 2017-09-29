def advanced_text_submissions():
    L = []
    with open("advanced_submissions.txt", "a+") as fp:
        while True:
            a = raw_input("Enter anything ")
            if a == 'SAVE':
                for i in L:
                    fp.write(i)
                fp.close()
                fp = open("advanced_submissions.txt", "a+")
                L = []
            elif a == 'CLOSE':
                for j in L:
                    fp.write(j)
                fp.close()
                break
            else:
                L.append(a + '\n')


advanced_text_submissions()
