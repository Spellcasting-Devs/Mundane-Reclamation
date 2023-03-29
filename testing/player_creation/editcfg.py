from configparser import ConfigParser



def edit():
    config = ConfigParser()
    config.read("tester.ini")
    
    config["CHAPTER1"]["c1"] = "True"
    
    with open("tester.ini", "w") as configfile:
        config.write(configfile)

edit()