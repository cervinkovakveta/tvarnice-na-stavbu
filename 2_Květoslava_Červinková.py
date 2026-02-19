
# základní informace o programu
"""
Program po správném přihlášení, vypočítá kolik je potřeba tvárnic na stavbu podle zadaných rozměrů stěn a oken.
A zobrazí pobočky, které mají potřebné množství tvárnic na skladě. 

Identifikační údaje o autorovi projektu:
    Jméno a příjmení: Květoslava Červinková

Přihlašovací údaje:
    Uživatelské jméno: stavebnik
    Heslo: stavba
"""
# definuje funkce na výpočet: plocha stěny včetně okna, plocha okna, plocha stěny bez okna a počet potřebných tvárnic
def vypoctet_plochy_objektu(a, b):
   """
   Funkce vypocet_plochy_objektu() vypočítá plochu v m2

   :param a: délka(výška) objektu zadaná v metrech
   :param b: výška(šířka) objektu zadaná v metrech
   :return: Výsledek násobení plochy v m2 
   """
   plocha_objektu = a * b
   return plocha_objektu

def vypocet_steny_bez_okna(a, b):
   """
   Funkce vypocet_steny_bez_okna() vypočítá přesnou plochu v m2 stěny bez oken, 
   odečte plochu okna od plochy stěny

   :param a: plocha stěny v m2
   :param b: plocha okna v m2 
   :return: Výsledek plochy stěny v m2 bez okna
   """
   stena_bez_okna = a - b
   return stena_bez_okna

def pocet_tvarnic(a, b):
   """
   Funkce pocet_tvarnic() vypočítá kolik je potřeba ks na stavbu stěny bez okna

   :param a: plocha stěny bez okna v m2
   :param b: dělitel (plocha jedné tvárnice, která bude použitá ke stavbě)
   :return: počet ks potřebných ke stavbě stěny
   """
   potrebne_ks_tvarnic = a / b
   return potrebne_ks_tvarnic

# nastavení uživatelského jména a hesla
spravne_jmeno = "stavebnik"
spravne_heslo = "stavba"

# nadpis konfigurátoru
print("\nKonfigurátor zdícího systému")
print("*" * 28)
print()

# program zkontroluje vložené uživatelské jméno a heslo
uzivatelske_jmeno = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")

# nastaví podmínku při zadání správných přihlašovacích údajů pokračuje v programu, 
# při zadaní špatných program ukončí
if uzivatelske_jmeno != spravne_jmeno or heslo != spravne_heslo:
   print("Zadali jste chybné jméno nebo heslo!")
   exit()

print()

# program načte rozměry stěny a okna od uživatele
delka_steny = float(input("Zadejte délku stěny (metry): "))
vyska_steny = float(input("Zadejte výšku stěny (metry): "))
vyska_okna = float(input("Zadejte výšku okna(metry): "))
sirka_okna = float(input("Zadejte šířku okna (metry): "))
print()

# program načte plochu tvárnice v m2
plocha_tvarnice = 0.1

# zavolá funkce na vypočet plochy a vypíše
vysledek_plocha_steny = vypoctet_plochy_objektu(delka_steny, vyska_steny)
print(f"Plocha stěny včetně okna: {vysledek_plocha_steny} m^2")

vysledek_plocha_okna = vypoctet_plochy_objektu(vyska_okna, sirka_okna)
print(f"Plocha okna: {vysledek_plocha_okna} m^2")

vysledek_steny_bez_okna = vypocet_steny_bez_okna(vysledek_plocha_steny, vysledek_plocha_okna)
print(f"Plocha stěny bez okna: {vysledek_steny_bez_okna} m^2")

# zavolá funkci na výpočet kolik je potřeba tvárnic
pocet_tvarnic_celkem = int(pocet_tvarnic(vysledek_steny_bez_okna, plocha_tvarnice))
print(f"Počet tvárnic potřebných k vyzdění plochy stěny: {pocet_tvarnic_celkem} ks")


# vytvoří hlavičku tabulky
hlavicka_tabulky = ("Město", "Druh materiálu", "Počet kusů na pobočce")

# vytvoří seznam poboček s dostupností tvárnic
pobocky = [
    ("Praha", "tvárnice", 500), 
    ("Brno", "tvárnice", 300), 
    ("Ostrava", "tvárnice", 700)
]

# vypíše nadpis tabulky
print()
print("Dostupnost materiálu na pobočkách v ČR")
print("*" * 38)

# výpiše hlavičku tabulky
print(f"| {hlavicka_tabulky[0]:8} | {hlavicka_tabulky[1]:14} | {hlavicka_tabulky[2]:22} |")
print("*" * 54)

# výpis dat do tabulky podle množství tvárnic

for mesto, material, pocet_ks in pobocky:
   if pocet_ks >= pocet_tvarnic_celkem: 
      print(f"| {mesto:8} | {material:14} | {pocet_ks:<22} |")

print()

