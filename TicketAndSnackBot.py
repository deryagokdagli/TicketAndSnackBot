import random
fiyatlar = {"Bilet" : 120, "Su" : 10, "Kola" : 35, "Patlamış Mısır" : 50}
koltuklar = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
print("Hoş geldiniz, lütfen almak istediğiniz ürünleri seçin.")
for (key,value) in fiyatlar.items():
    print(f"- {key} : {value}")

def hesapla(bilet,su,kola,patlamisMisir):
    toplam = (bilet * fiyatlar["Bilet"] + su * fiyatlar["Su"] + kola * fiyatlar["Kola"] + patlamisMisir * fiyatlar["Patlamış Mısır"])
    return (f"Toplam ödeme tutarınız: {toplam}")

bilet = int(input("Kaç adet bilet almak istiyorsunuz?"))
if bilet > 0:
    secilenKoltuklar = random.sample(koltuklar, bilet)
    print("Koltuk(lar)ınız otomatik olarak atanıyor...")
    print("Atanan koltuk(lar): " + ", ".join(secilenKoltuklar))
su = int(input("Kaç adet su almak istiyorsunuz?"))
kola = int(input("Kaç adet kola almak istiyorsunuz?"))
patlamisMisir = int(input("Kaç adet patlamış mısır almak istiyorsunuz?"))
print(hesapla(bilet,su,kola,patlamisMisir))