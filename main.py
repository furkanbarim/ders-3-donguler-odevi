# Ödev: 1'den kullanıcının girdiği sayıya kadar
# olan sayıların eğer tek ise karesini , çift ise küpünün
# toplamını ayrı ayrı hesaplayan kod parçacığı

baslangic: int = 1
bitis: int = int(input("lütfen bir sayı gir: "))
tek_kare_toplam = 0
cift_kup_toplam = 0



if bitis < 1:
    print("lütfen 1 den büyük bir sayı olmalıdır")
else:
    while baslangic <= bitis:
        if baslangic % 2 == 0:
            cift_kup_toplam += baslangic**3
        else:
            tek_kare_toplam += baslangic**2

        baslangic += 1

print(f"tek sayıların toplamı: {tek_kare_toplam}")
print(f"çift sayıların toplamı: {cift_kup_toplam}")





