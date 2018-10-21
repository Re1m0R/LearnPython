def elements_sum(taisarv):

    # Funktsioon liidab arve kokku alates 1 kuni etteantud arvuni. Loop kasvatab järjekorra numbrit 1 ja liidab selle eelmisele (+1 seetõttu, et alustan 0-st).

    tulemus=0

    i=0

    while i<taisarv:

        tulemus=tulemus+i+1

        i=i+1

    return tulemus

def time_convert(aeg):

    # Funktsioon leiab, palju minuteid on keskööst möödunud. Kõigepealt löön sisendi tükkideks, konverteerin möödunud tunnid minutiteks ning seejärel liidan minutitele juurde.

    algparameetrid=aeg.split(":")

    tunnid=int(algparameetrid[0])-0

    minutid=int(algparameetrid[1])

    tulemus=tunnid*60+minutid

    return tulemus

def sort_values(string):

    # Funktsioon eraldab numbrid ja tähed, järjestab nad kasvavas järjekorras ning kujundab kaheks plokiks new sümboliga.

    algnestring=string.split(",")

    i=0

    stringipikkus=len(algnestring)

    numbrid = []

    tahed=[]

    tulemus = ""

    # Kõigepealt eraldan numbrid ja tahed ning  järjestan nad.

    while i<stringipikkus:

        if algnestring[i].isnumeric()==True:

            numbrid.append(int(algnestring[i]))

        elif algnestring[i].isalpha()==True:

            tahed.append(algnestring[i])

        i=i+1

    numbrid.sort()

    tahed.sort()

    # Seejärel hakkan stringi kokku õmblema.

    for element in numbrid:

        tulemus=tulemus+str(element)+" "

    tulemus=tulemus + "\n"

    for element in tahed:
        tulemus=tulemus + element + " "

    return tulemus

#Siin on master kood, mis laseb järjest ülesandeid kontrollida.

Sisend=int(input("Palun sisestage esimese ülesande sisend (täisarv)! "))

print(elements_sum(Sisend))

Sisend=input("Palun sisestage teise ülesande sisend (hh:mm)! ")

print(time_convert(Sisend))

Sisend=input("Palun sisestage kolmanda ülesande sisend (komaga eraldatud tähed või numbrid)! ")

print(sort_values(Sisend)