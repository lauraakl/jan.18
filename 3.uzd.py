def lasit_datni():
    try:
        with open("uzd.txt","r", encoding='utf8') as datne:
            datne.write("lauka ir auksti")


    except FileNotFoundError:
        print("datne nav atrasta")


if __name__=="__main__":
    lasit_datni()