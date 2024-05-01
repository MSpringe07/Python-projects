import pandas as pd

# Atver Excel failu
fails = pd.ExcelFile('dati_masiviem_og.xlsx')

df = []
for lapa in fails.sheet_names: # Cikls, kas piekļūst visām darba lapām
    df.append(fails.parse(lapa)) # Ievietojam katru darba lapu sarakstā
# Viss Excel faila saturs - varēsim tālāk apstrādām


# Aprēķiniet kolonnas "Kopā" un "Peļņa".
df[0]['Cena'] = df[0]['Pašizmaksa'] * 1.33 * 1.21
df[0]['Kopā'] = df[0]['Cena'] * df[0]['Skaits']
df[0]['Peļņa'] = df[0]['Kopā'] - df[0]['Pašizmaksa']* df[0]['Skaits']

# Saglabā datus lapā
with pd.ExcelWriter('dati_masiviem_og.xlsx', mode='a', engine='openpyxl') as writer:
    df[0].to_excel(writer, sheet_name='Sheet1_original', index=False)

df[0].to_excel('dati_masiviem_og.xlsx', sheet_name='Sheet1', index=False)

# Aprēķina kopējo kases aparātā saņemto naudas summu, pārdoto grāmatu skaitu un kopējo peļņu
total_money = df[0]['Kopā'].sum()
total_books = df[0]['Skaits'].sum()
total_profit = df[0]['Peļņa'].sum()

# Saglabā datus lapā
summary = pd.DataFrame({'Iekasētā nauda': [total_money], 'Kopā Grāmatas': [total_books], 'Kopējā peļņa': [total_profit]})

# Pievieno kopsavilkumu faila df_copy beigām
df_copy = df[0]._append(summary)

# Saglabā datus lapā
with pd.ExcelWriter('dati_masiviem_og.xlsx', mode='a', engine='openpyxl') as writer:
    df_copy.to_excel(writer, sheet_name='Sheet2', index=False)

# Grupē datus pēc "Datuma". Jāievada "Datums", "Numurs" un "Kopā".
grouped = df[0].groupby('Datums').agg({'Skaits': 'sum', 'Kopā': 'sum'}).reset_index()

# Saglabā iegūto rezultātu atsevišķā lapā
with pd.ExcelWriter('dati_masiviem_og.xlsx', mode='a', engine='openpyxl') as writer:
    grouped.to_excel(writer, sheet_name='Pēc datumiem', index=False)

# Atrod grāmatu, kuras nosaukums sākas ar tava vārda vai uzvārda pirmo burtu
starts_with_M = df[0]['Nosaukums'].str.startswith('M')

filtered_titles = df[0][starts_with_M]

filtered_titles = filtered_titles[['Nosaukums', 'Skaits', 'Kopā']]

# Saglabā iegūto rezultātu atsevišķā lapā
with pd.ExcelWriter('dati_masiviem_og.xlsx', mode='a', engine='openpyxl') as writer:
    filtered_titles.to_excel(writer, sheet_name='Filtrētās grāmatas', index=False)

chosen_date = '2020-09-18'  # Mainiet to uz izvēlēto datumu
# Konvertējiet kolonnu Datums datuma un laika formātā
df[0]['Datums'] = pd.to_datetime(df[0]['Datums'])
# Filtrējiet DataFrame pēc izvēlētā datuma
filtered_by_date = df[0][df[0]['Datums'] == chosen_date]
filtered_by_date = filtered_by_date[['Datums', 'Nosaukums', 'Skaits', 'Kopā']]
# Saglabā iegūto rezultātu atsevišķā lapā
with pd.ExcelWriter('dati_masiviem_og.xlsx', mode='a', engine='openpyxl') as writer:
    filtered_by_date.to_excel(writer, sheet_name='Filtrētie datumi', index=False)