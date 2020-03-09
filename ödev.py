print("sağlık göstergesi hesaplama")
ağırlık=float(input("ağırlığınızı girin(kg):"))
boy=float(input("boy girin(cm):"))
bki=ağırlık/((boy/100)*2)
print("bki değeri:",bki)
print("dünya sağlık örgütüne göre")
if bki<18.5:
    print("zayıf")
    print("{} kilo almanız gerekiyor.".format(round(18.5*((boy/100.0)*2)-ağırlık)))
elif bki<=25:
    print("sağlıklı,tebrikler")
elif bki<=30:
    print("az kilolu")
    print("{} kilo vermeniz gerekiyor.".format(round(ağırlık-25*((boy/100.0)*2))))
elif bki<=35:
    print("1.obez")
    print("{} kilo vermeniz gerekiyor.".format(round(ağırlık-25*((boy/100.0)*2))))
else:
    print("3.obez")
    print("{} kilo vermeniz gerekiyor.".format(round(ağırlık-25*((boy/100.0)*2))))