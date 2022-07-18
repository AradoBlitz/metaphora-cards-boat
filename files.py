import os, random

man_cards = [x for x in os.listdir("./cards/man/") if os.path.isfile(os.path.join("./cards/man/", x))]

woman_cards= os.listdir("./cards/woman/")

def selectCard(sex, sphere_life):
    values =  "./cards/" + sex + "/" + sphere_life + "/" + random.choice(os.listdir("./cards" 
    + "/" + sex + "/" + sphere_life))
    return values

