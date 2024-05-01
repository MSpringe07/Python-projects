# Vilcienu uzdevums
zils_v = 57 
zals_v = 60 
t_zils = 10/60 
t_sarkanais = 4 
rj = 43 
vr = 168
sarkanais_v = 60


km_no_Rigas = rj - (t_zils * zils_v) 
print("Pēc 10 minūtēm starp vilcieniem ir" , km_no_Rigas , "km") 

kop_atrums = zals_v + zils_v  

laiks_satiksies = km_no_Rigas / kop_atrums
print( "Vilcieni satiksies pēc" , laiks_satiksies*60 , "minūtēm") 

kur_satiksies = laiks_satiksies * zals_v
print(" Vilcieni satiksies", kur_satiksies ,"km no rīgas.") 

sarkanais_attalums = sarkanais_v * t_sarkanais
print("Sarkanais vilciens 4stundās ir nobraucis", sarkanais_attalums," km ")
print("Sarkanais vilciens ir Jelgavā") 

if (sarkanais_attalums < rj) :
    print("Vilciens ir starp VAlku un Rīgu")
elif (sarkanais_attalums == vr): 
       print(" Vilciens ir Rīgā")
else:
      print(" Vilciens ir garām Rīgai")


# Fermu uzdevums

aitas = 225
strausi = 15
vilnasCena = 20.5
olasCena = 30
oluSkaits = 15
oluPelna = oluSkaits * olasCena * strausi
print( "Visas olas maksās:" , oluPelna , "EUR")
vilnasPelna = aitas * vilnasCena
print("Vilnu pārdos par: " , vilnasPelna ,"EUR") 

# Ūdens uzdevums

rigas_u = 1.79
zaku_u = 7.83
venden_u = 8.89
rigas_u_litri = 1000
zaku_u_litri = 18.9
venden_u_litri = 19.9

rigas_litra = rigas_u / rigas_u_litri
zaku_litra = zaku_u / zaku_u_litri
venden_litra = venden_u /venden_u_litri

sarp_VR = venden_litra - rigas_litra
starp_RZ = rigas_litra - zaku_litra
sarp_RV = rigas_litra - venden_litra
starp_ZR = zaku_litra - rigas_litra


if (zaku_litra < venden_litra): 
    print(" Zaķumuižas ūdens ir lētāks par Venden ūdeni, tas makā", round(zaku_litra,2), "eur/l")
      
else:
   print("Venden ūdens ir lētāks par Zaķumuižas ūdeni, tas maksā", round(venden_litra,2), " eur/l")


if (rigas_litra < venden_litra):
    print("Rīgas ūdens ir lētāks nekā pudelē esošais ūdens!")       
elif (zaku_litra < rigas_litra):
     print( "Zaķumuižas ūdens ir lētāks nekā Rīgas ūdens!")
elif (rigas_litra < zaku_litra):
    print(" Rīgas ūdens ir lētāks nekā pudelē esošais ūdens!")
elif (venden_litra < rigas_litra):
    print("Venden ūdens ir lētāks nekā Rīgas ūdens!")

if (venden_litra > rigas_litra):
    print("Venden ūdens ir lētāks par " ,round(sarp_VR,2) ,"eur!")
else:

    print("Rīgas ūdens ir lētāks par ",round(sarp_RV,2) ,"eur!")
   