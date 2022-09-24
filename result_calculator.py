def get_wpm(time,userinput,words):
    gross_wpm=(len(userinput)/5)/(float(time)/ 60)
    net_wpm =1
    accuracy = 1
    print(gross_wpm,len(userinput),time)