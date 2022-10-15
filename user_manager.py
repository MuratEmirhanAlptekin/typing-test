def userlogin(username):
    userdb = open("userdb.txt","r")
    for i in userdb:
        if username in i:
            return i
    userdb.close()
    language = input("what language do you want to play with on this username ")
    word_amount = input("how many words do you want to play with ? ")
    userdb = open("userdb.txt","a")
    userdb.write(username+" ")
    userdb.write(language+" ")
    userdb.write(word_amount+" ")
    userdb.write("\n")
    userdb.close()
    return (username+language+word_amount)
a = userlogin("hanbaba")