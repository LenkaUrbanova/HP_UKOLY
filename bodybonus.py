import json

with open("UKOLY/bodyBonus.json", encoding='utf-8') as file:
    studenti_s_bonusem = json.load(file)

with open("UKOLY/body.json", encoding='utf-8') as file:
    seznam_studentu = json.load(file)

for key, value in seznam_studentu.items():
    if value >= 60:
        seznam_studentu[key] = "pass"
    else:
        seznam_studentu[key] = "fail"
