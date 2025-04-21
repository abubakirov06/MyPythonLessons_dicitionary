mahsulotlar = {'olma':1200, 'nok':4000, 'behi':4500, 'anjir':7000,
   'uzum':3800, 'o\'rik':4800}
for mahsulot in mahsulotlar:
    print(mahsulot)
    
mevalar = ['olma', 'anor', 'nok', 'ananas', 'banan', 'anjir']
for meva in mevalar:
    if meva in mahsulotlar:
        print(f"Bizda {meva} bor")
    else:
        print(f"Uzr, bizda {meva} yo'q")
izohli_lugat = {'integer':'butun son', 'float':"o'nli kasr", 'string':'matn',
'variable':"o'zgaruvchi", "dictionary":"lug'at", 'value':'qiymat', 'key':'kalit',
'if':'agar'}
for key, value in sorted(izohli_lugat.items()):
    print(f"kalit {key}")
    print(f"qiymat {value}")
davlatlar = {"Angliya":"London", 'Fransiya':'Parij', "Germaniya":"Berlin", 'Italiya':'Rim',
    'Misr':'Qohira', 'Turkiya':'Anqara', 'Rossiya':'Moskva', 'Xitoy':'Pekin',
    'Yaponiya':"Tokiyo", "O'zbekiston":'Toshkent'}
for davlat, poytaxt in sorted(davlatlar.items()):
    print(f"Davlat: {davlat}")
    print(f"Poytaxt: {poytaxt}")
country = input('Birorta davlat nomini kiriting:\n>>>')
if country.title() in davlatlar:
    print(f"{country.title()}ning poytaxti {davlatlar[country.title()]}")
else:
    print('Kechirasiz, bizda bu davlat haqida ma\'lumot yo\'q')
    
menu = {'manti':15000, 'chuchvara':17000, 'osh':40000, 'qozon kabob':60000, 'tandir kabob':80000,
        'qiyma shashlik':14000, 'jaz shashlik':18000, 'sho\'rva':25000,
        'steyk':45000, 'xonim':22000}
buyurtmalar = []
for n in range(0, 3):
    buyurtma = input(f'{n+1}ga qanday taom buyurtma qilmoqchisiz?\n>>>')
    buyurtmalar.append(buyurtma)
for taom in buyurtmalar:
    if taom in menu:
        print(f"{taom.title()}ning narxi {menu[taom.lower()]}")
    
    else:
        print(f"Kechirasiz, bizda {taom.lower()} yo'q")

