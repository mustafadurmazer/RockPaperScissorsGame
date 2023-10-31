import random


#print("Taş Kağıt Makas Oyununa Hoşgeldiniz")
list = ["T","K","M"]
print("Oyundan Çıkmak İçin 'E'ye Basınız\n")
sayacpc = 0
sayackullanıcı = 0


while 1:
    rastgele = random.choice(list)
    kullanıcı = input("Seçim Yapınız(T,K,M,E)\n")
    if kullanıcı in list :
            if kullanıcı == "E":
                print(f"Oyun Bitti Kullanıcı :{sayackullanıcı}, Bilgisayar :{sayacpc}")
                break

            elif rastgele == kullanıcı:
                print("Aynı seçeneği seçtiniz.Tekrar deneyiniz")
                continue
            elif rastgele == "T":
                if kullanıcı == "M":
                    sayacpc += 1
                    print(f"Kaybettiniz.Kullanıcı :{sayackullanıcı}, Bilgisayar: {sayacpc}")
                else:
                    sayackullanıcı += 1
                    print(f"Tebrikler! kazandınız.Kullanıcı :{sayackullanıcı}, Bilgisayar: {sayacpc} ")
            elif rastgele == "M":
                if kullanıcı == "K":
                    sayacpc += 1
                    print(f"Kaybettiniz.Kullanıcı :{sayackullanıcı}, Bilgisayar: {sayacpc}")
                else:
                    sayackullanıcı += 1
                    print(f"Tebrikler! kazandınız.Kullanıcı :{sayackullanıcı}, Bilgisayar: {sayacpc} ")
            elif rastgele == "K":
                if kullanıcı == "T":
                    sayacpc += 1
                    print(f"Kaybettiniz.Kullanıcı :{sayackullanıcı}, Bilgisayar: {sayacpc}")
                else:
                    sayackullanıcı += 1
                    print(f"Tebrikler! kazandınız.Kullanıcı :{sayackullanıcı}, Bilgisayar: {sayacpc}")
    else:
            print("Yanlış Seçim! Tekrar Deneyiniz")


