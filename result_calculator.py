def get_wpm(time,userinput,words):
    correctlist = []
    gross_wpm=(len(userinput)/5)/(float(time)/ 60)
    net_wpm =1
    accuracy = 1
    for i,j in zip(userinput.split(),words.split()):
        if i==j:
            correctlist.append(i)
    correct_word = " ".join(correctlist)
    wpm = (len(correct_word)/5) / (float(time)/60)
    return (wpm,gross_wpm)
