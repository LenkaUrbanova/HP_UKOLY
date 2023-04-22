import json
#POZOR nechat v [] dle zadání- není to slovník!

with open("UKOLY/body.json", encoding='utf-8') as file:
    seznam_studentu = json.load(file)

for key, value in seznam_studentu.items():
    if value >= 60:
        seznam_studentu[key] = "pass"
    else:
        seznam_studentu[key] = "fail"

# print(seznam_studentu) 


with open("UKOLY/pryToMamprepsat.json", mode="w", encoding='utf-8') as file:
    json.dump(seznam_studentu, file, ensure_ascii=False)


  
 





