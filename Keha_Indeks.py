print("Tere! Olen sinu uus sõber - Python!")
nimi=input("Sisesta oma nimi:")
print(f"{nimi}, oi kui ilus nimi! ")
try:
    soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei, 1-jah => "))
    if soov==1:
        print("Indeksi leidmine")
        try:
            pikkus=int(input("Mis on sinu pikkus"))
            try:
                mass=float(input("mis on sinu kaal"))
                indeks=mass/(0.1*pikkus)**2
                print(nimi,"! Sinu keha indeks on:",indeks)
            except:
                print("vale kaal formaat")

        except:
            print("vale pikkuse formaat")
    elif soov==0:
        print("Kahju! See on vaga kasulin info")
    else:
        print("vale valik. saab valida ainult 1 voi 0")
except:
    print("Vale soov!")