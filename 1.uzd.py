def lasit_datni():
    try:
        with open('1.uzd.txt',"w", encoding='utf8') as datne:
            datne.write(input("ievadi tekstu: "))

    except FileNotFoundError:
        print("datne nav strasta!")


        if __name__=="__main__":
            lasit_datni()

"""
ASCII
"""