def lasit_datni():
    try:
        with open("uzd.txt","w", encoding='utf8') as datne:
            datne.write("vai ara snieg?")


    except FileNotFoundError:
        print("datne nav atrasta")


if __name__=="__main__":
    lasit_datni()
