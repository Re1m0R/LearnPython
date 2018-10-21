def ruutvõrrand(a, b, c):

    from math import sqrt

    D = b * b - 4 * a * c

    kaust = open("Tulemused.txt", "a")

    if D < 0:

        kaust.write("No roots. \n")

    else:

        tulem1 = (-b + sqrt(D)) / 2 * a

        tulem2 = (-b - sqrt(D)) / 2 * a

        kaust.write(str(tulem1) + ", " + str(tulem2) + "\n")

    kaust.close()

def lineaarvõrrand(b, c):

    kaust = open("Tulemused.txt", "a")

    tulem = -c/b

    kaust.write(str(tulem) + "\n")

while True:
    a = int(input("Palun sisestage A: "))
    b = int(input("Palun sisestage B: "))
    c = int(input("Palun sisestage C: "))

    if a == 0:
        lineaarvõrrand(b, c)
    else:
        ruutvõrrand(a, b, c)