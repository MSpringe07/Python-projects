# FizzBuzz
Skaitlis = 1
Tris = 3
Pieci = 5
PiecPac = 15

while (Skaitlis <= 100) :
    if (Skaitlis % PiecPac == 0 ):
        print("FizzBuzz!")
    elif (Skaitlis % Tris == 0):
        print("Fizz!") 
    elif (Skaitlis % Pieci == 0):
      print("Buzz!")
    else:
       print(Skaitlis)
    Skaitlis = Skaitlis + 1

#Algas uzdevums

ALGAS_B = 0.15
NOST_GADI = 5
MENESA_ALGA = 1000
MIN_GADI = 2

if (NOST_GADI > MIN_GADI):
    print("Nostrādātie gadi ir" , NOST_GADI)
elif (NOST_GADI < MIN_GADI):
    print("Bonusu nesaņem!")
else:
    print("Bonusu nesaņem!")

Bonussa_gadi = NOST_GADI - MIN_GADI
if (Bonussa_gadi < 0):
    print("Bonusu nesaņem.")
else:
    Bonuss = ALGAS_B * Bonussa_gadi * MENESA_ALGA
    print("Algas bonuss ir" , round(Bonuss, 2))
    
#Pilsētas uzdevums

Iedzivotaji = 1000
KGProc = 2
KGMainas = 50
SasIedzSK = 5000
Gads = 0
   
while (Iedzivotaji < SasIedzSK):
    Iedzivotaji = Iedzivotaji + Iedzivotaji * KGProc + KGMainas
    Gads = Gads + 1
    if (Iedzivotaji <= 0 ):
        Gads = -1
        break
if (Gads < 0):
   print("Iedzīvotāju skaitu nesasniegs!")
else:
    print("Iedzīvotāju skaitu sasniegs" ,Gads , "gados!")

#Pirmskaitļu uzdevums

skaitlis = int(input("Ievadiet skaitli: "))

pirmskaitlis = False

if skaitlis == 1:
    print(skaitlis, "nav pirmskaitlis")
elif skaitlis > 1:
    for i in range(2, skaitlis):
        if (skaitlis % i) == 0:
            pirmskaitlis = True
            break

    if pirmskaitlis:
        print(skaitlis, "nav pirmskaitlis")
    else:
        print(skaitlis, "ir pirmskaitlis")