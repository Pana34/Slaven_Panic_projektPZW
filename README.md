# Web aplikacija za upravljanje budžetom

## 📌 Opis zadatka
Ova aplikacija omogućuje korisnicima upravljanje osobnim financijama putem sljedećih funkcionalnosti:
- Kreiranje, pregled, uređivanje i brisanje **budžeta, prihoda, rashoda i kategorija budžeta**.
- Prikaz **popisa svih stavki** s mogućnošću filtriranja.
- **Interaktivni grafikoni** koji vizualiziraju financijske podatke.
- **RESTful API** za rad s modelima putem API endpointa.

Aplikacija je implementirana koristeći **Django**, **Django REST Framework** i **Tailwind CSS**.

## Funkcionalnosti aplikacije
1. ### CRUD operacije za budžete, prihode, rashode i kategorije:
   - Kreiranje novih stavki.
   - Pregled svih stavki uz filtriranje.
   - Uređivanje i brisanje stavki.
2. **REST API**:
   - Endpointi za dohvat, kreiranje, uređivanje i brisanje modela putem API-ja.
   - Zaštita API-ja autentifikacijom (korisnici moraju biti prijavljeni).
3. **Autentifikacija korisnika**:
   - Korisnici se moraju prijaviti za korištenje aplikacije i API-ja.
   - Registracija i prijava putem ugrađenih formi.
4. **Grafički prikazi podataka**:
   - Bar Chart: Raspodjela budžeta po kategorijama
   - Pie Chart: Omjer prihoda i rashoda
   - Line Chart: Financijski trendovi kroz mjesece
   - Podaci se dohvaćaju **dinamički preko API-ja** i prikazuju putem **Chart.js**  

## Informacije o studentu
- **Ime i prezime**: Slaven Panić
- **Fakultet**: Fakultet informatike i digitalnih tehnologija
- **Kolegij**: Programiranje za web
