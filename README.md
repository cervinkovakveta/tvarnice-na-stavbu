# tvarnice-na-stavbu
Program po správném přihlášení, vypočítá kolik je potřeba tvárnic na stavbu podle zadaných rozměrů stěn a oken. A zobrazí pobočky, které mají potřebné množství tvárnic na skladě.
Python skript určený pro stavební výpočty a kontrolu skladové dostupnosti materiálu. Program vypočítá přesnou spotřebu tvárnic na základě rozměrů stěn a otvorů (oken) a následně vyfiltruje pobočky, které mají dostatečné zásoby.

Přístup do systému je chráněn uživatelským jménem a heslem.
Logika je rozdělena do znovupoužitelných funkcí (vypocet plochy, odečet otvorů, výpočet kusů).
Program porovnává vypočtenou potřebu s reálnými stavy na pobočkách (Praha, Brno, Ostrava).
Výsledky jsou prezentovány v přehledné textové tabulce.

Přihlašovací údaje
* **Uživatelské jméno:** `stavebnik`
* **Heslo:** `stavba`
