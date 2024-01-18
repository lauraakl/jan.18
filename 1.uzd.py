def lasit_datni():
    try:
        with open('1.uzd.txt',"r", encoding='utf8') as datne:
            print(datne.readline())
            print(datne.readline())

    except FileNotFoundError:
        print("datne nav strasta!")


        if __name__=="__main__":
            lasit_datni()
