import os, random

cards_dir = os.getenv('CARDS_DIR')

man_cards = [x for x in os.listdir(cards_dir + "/man/") if os.path.isfile(os.path.join(cards_dir + "/man/", x))]

woman_cards= os.listdir(cards_dir + "/woman/")

def selectCard(sex, sphere_life):
    values =  cards_dir + "/" + sex + "/" + sphere_life + "/" + random.choice(os.listdir(cards_dir 
    + "/" + sex + "/" + sphere_life))
    return values

