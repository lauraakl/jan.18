def lasit_datni():
    try:
        with open('uzd.txt',"w", encoding='utf8') as datne:
            datne.write("ara snieg sniegs ")

    except FileNotFoundError:
        print("datne nav strasta!")


        if __name__=="__main__":
            lasit_datni()

"""
ASCII
"""