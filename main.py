import words_manager
import result_calculator 
import user_manager
from datetime import datetime
from os import path
from time import sleep

def start(username):
    user_manager.userlogin(username)
    userdb = open("userdb.txt" , "r" )
    for i in userdb:
        if username in i:
            username , language, word_amount = i.split()
            word_amount = int(word_amount)
            print(username , language, word_amount)
    words = words_manager.get_words(word_amount,language)
    print("   ",*words)
    sleep(1)
    start_time = datetime.now()
    userinput = input("GO!!")
    finish_time = datetime.now()
    time_taken = round((finish_time - start_time).total_seconds(), 1) 
    time_taken = str(time_taken)
    words = " ".join(words)
    result_calculator.get_wpm(time_taken,userinput,words)
    result = open("resultdb.txt","a")
    result.write(username+" ")
    result.write(time_taken+" ")
    result.write(words+" ")
    result.write("\n")


if __name__ == '__main__':
    username = input("enter your username ")
    while True:
        choice_screen = input("1.play 2.view stats 3.Leaderboard 0.Exit")
        if choice_screen == "1":
            start(username)
        if choice_screen == "2":
            pass
        if choice_screen == "3":
            pass
        if choice_screen == "0":
            break