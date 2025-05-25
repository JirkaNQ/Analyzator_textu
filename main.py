print("""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Jiří Nusko
email: nusko@seznam.cz
""")
# zakladni udaje
TEXTS  = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
uzivatele = {
    "bob":"123", 
    "ann": "pass123", 
    "mike":"password123", 
    "liz": "pass123"
    }
jmeno = input("Zadej sve jmeno:")
heslo = input("Zadej sve heslo:")
print("-" * 50)
for user in uzivatele:
    if uzivatele.get(jmeno) == heslo: # test zda jmeno exituje a heslo je spravne
        print("Welkome to the app,", jmeno)
        print("We have 3 texts to be analysed.")
        print("-" * 50)
        number_odstavec = int(input("Enter a number btw. 1 and 3 to select: ")) #výběr textu (odstavce) jako číslo
        print("-" * 50)
        if number_odstavec == 1 or number_odstavec == 2 or number_odstavec == 3: 
            # výběr odstavce a převedení na list jednotlivých slov
            odstavec = str.split(TEXTS[number_odstavec - 1], sep=None)
            pocet_slov = len(odstavec) #určení počtu slov v odstavci
            vsechna_velka = 0
            pocatecni_velka = 0
            vsechna_mala = 0
            cisla = 0
            suma_cisel = 0
            new_odstavec = list()
            for slovo in odstavec:
                slovo = slovo.strip(".,") # odstranění "," a "." ze slov
                new_odstavec.append(slovo)
            vsechna_cisla = list()
            vsechna_slova_jako_cisla = list()
            cetnost_slov = dict()
            for slovo in new_odstavec:
                if slovo.istitle(): # zjištění počtu slov s velkým písmenem na počátku
                        pocatecni_velka += 1
                if slovo.islower(): # zjištění počtu slov se všemi písmeny malými
                        vsechna_mala += 1
                if slovo.isupper(): # zjištění počtu slov se všemi písmeny velkými
                        vsechna_velka += 1
                if slovo.isnumeric(): # zjištění počtu čísel a jejich suma
                        cisla += 1
                        vsechna_cisla.append(int(slovo))
                        suma_cisel = sum(vsechna_cisla)           
                slovo = len(slovo)
                vsechna_slova_jako_cisla.append(slovo)
                max_slovo = max(vsechna_slova_jako_cisla)
            #počítání slov dle jejich četnosti
            for cislo in vsechna_slova_jako_cisla: 
                if cislo in cetnost_slov:
                    cetnost_slov[cislo] += 1
                else:
                    cetnost_slov[cislo] = 1  
            #tisk výsledků        
            print("There are", pocet_slov, "words in the selected text.")
            print("There are", pocatecni_velka, "titlecase words.")
            print("There are", vsechna_velka, "uppercase words.")
            print("There are", vsechna_mala, "lowercase words.")
            print("There are", len(vsechna_cisla), "numeric strings.")
            print("The sum of all the numbers is", suma_cisel)
            #print grafu četnosti jednotlivých slov
            print("-" * 50)
            print( "{:>4}|".format("LEN"),"OCCURENCES"," " * 5,"|NR.")
            print("-" * 50)
            for delka, pocet in sorted(cetnost_slov.items()):
                print("{:3}".format(delka),"|","*" * pocet," " * (max_slovo - pocet + 5), "|",pocet)                            
        else:
            print("nic nevybrano, konec")
        break
else:
    print(
    "user name:",jmeno,"\n",
    "password:", heslo,"\n", 
    "uregistered user, terminating the program ..."
    )
