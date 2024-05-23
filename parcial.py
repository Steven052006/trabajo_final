UrbanMt2 = 65000
Urban_permit = 0.80
CommercialMt2 = 34000
Commercial_permit = 0.34
CountryMt2= 50000
Country_permit= 0.10

ls_urban = []
ls_commercial = []
ls_country = []

import os 
def fnt_clear ():
    os.system('cls')
    print("Welcome to the Urban Planning Program")
    print("-------------------------------------")
    print("date : 25 to april to 2024 \n")
    
def fnt_register(name, width, length, type_lot):
    if type_lot == "Urban":
        value_mt2 = UrbanMt2
        permit_construction = Urban_permit
    elif type_lot == "Commercial":
        value_mt2 = CommercialMt2
        permit_construction = Commercial_permit
    elif type_lot == "Country":
        value_mt2 = CountryMt2
        permit_construction = Country_permit
    else:
        value_mt2 = 0
        permit_construction = 0
    area_lot = width * length
    value_lot = area_lot * value_mt2
    permit_lot = area_lot * permit_construction
    if value_lot > permit_lot:
        print(f"\n{name} has a permit of {permit_lot:.2f} mt2")
        print(f"{name} has a value of {value_lot:.2f} mt2")
        print(f"the total value is {value_lot + permit_lot:.2f}")
def fnt_selector(op):
    global sw 
    if op == '1':
        name = input('Name: ')
        width = float(input("Enter the width of the lot (in meters): "))
        length = float(input("Enter the length of the lot (in meters): "))
        type_lot = input('<<<< MENU OF LOTS >>>>>\n1. Urban\n2. Commercial\n3. Country\n -> ')
        if type_lot == "1":
            type_lot = "urban"
            R = {'name' : name, 'Area':width * length,'type lot':type_lot } 
            ls_urban.append = (R)
ls_commercial = []
ls_country = []

def fnt_register(name, width, length, type_lot):
    with open('lotes.txt', 'a') as f:
        f.write(f'{name},{width},{length},{type_lot}\n')

def fnt_clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def fnt_selector(op):
    if op == '1':
        fnt_clear()
        name = input('Enter the lot name: ')
        width = float(input('Enter the width of the lot: '))
        length = float(input('Enter the length of the lot: '))
        type_lot = input('Enter the lot type (1: Urban, 2: Commercial, 3: Country): ')
        if type_lot == "1":
            type_lot = "Urban"
            R = {'name': name, 'Area': width * length, 'Type lot': type_lot}
            ls_urban.append(R)
        elif type_lot == "2":
            type_lot = "Commercial"
            R = {'nombre': name, 'Area': width * length, 'type lot ': type_lot}
            ls_commercial.append(R)
        elif type_lot == "3":
            type_lot = "Country"
            R = {'name': name, 'Area': width * length, 'type_lot': type_lot}
            ls_country.append(R)
        fnt_register(name, width, length,type_lot )
        enter = input('<ENTER>')
    elif op == '2':
        fnt_clear()
        print('Urban Lots:')
        for lote in ls_urban:
            print(lote)
        print('Commercial Lots:')
        for lote in ls_commercial:
            print(lote)
        print('Rural Lots:')
        for lote in ls_country:
            print(lote)
        enter = input('Press <ENTER> to continue')
    elif op == '3':
        sw = False

sw = True
while sw == True:
    fnt_clear()
    op = input('\n\n<<<< MAIN MENU >>>>\n1. REGISTER LOTS -> \n2. SHOW LOTS -> \n3. EXIT ->\n -> ')
    fnt_selector(op)