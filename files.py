import os, random

man_cards = [x for x in os.listdir("./карты для бота/мужчины/") if os.path.isfile(os.path.join("./карты для бота/мужчины/", x))]

woman_cards= os.listdir("./карты для бота/женщины/")

def selectCard(sex, sphere_life):
    values =  "./карты для бота/" + sex + "/" + sphere_life + "/" + random.choice(os.listdir("./карты для бота" 
    + "/" + sex + "/" + sphere_life))
    return values

