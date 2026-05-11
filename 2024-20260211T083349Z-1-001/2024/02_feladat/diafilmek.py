class Diafilmek:
    def __init__(self,cim,megj_ev,kockak_szama,szines_e):
            self.cim = cim
            self.megj_ev = int(megj_ev)
            self.kockak_szama = int(kockak_szama)
            self.szines_e = int(szines_e)
diafilmek = []
fajl = open ("2024-20260211T083349Z-1-001/2024/02_feladat/filmek.txt", "r", encoding="utf-8")
for sor in fajl:
     adatok = sor.strip().split(";")

     uj = Diafilmek( adatok[0], adatok[1],adatok[2],adatok[3])
     diafilmek.append(uj)    
fajl.close()

#3.2 feladat
print(f"Ennyi film adata szerepel a listában: {len(diafilmek)}")

#3.3 feladat
legregebbi = diafilmek[1]
for d in diafilmek:
    if d.megj_ev < legregebbi.megj_ev:
      legregebbi = d
print(f"A legrégebbi film cłme {legregebbi.cim}, megjelent {legregebbi.megj_ev}, kockák száma {legregebbi.kockak_szama}")

#3.5 feladat
talalt = False
#filmek = []
evszam = int(input("ADj meg egy evszamot: "))
for film in diafilmek:
     if film.megj_ev == evszam:
          #filmek.append(film)
          talalt = True
          print(f"{evszam}-ban született filmek: {film.cim}")
if not talalt:
     print("EBBEN az evben nincs film")

         

#3.6 feladat
osszes_kocka = 0
szines_db = 0
for film in diafilmek:
    if film.szines_e == -1:
        osszes_kocka += film.kockak_szama
        szines_db += 1
if szines_db > 0:
     atlag = osszes_kocka / szines_db
     print(f"A szines kockak atlagos hossza :{atlag: .2f}")

else:
     print("NIncs szines film")
