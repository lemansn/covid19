hasta_mas_takdimi = input('COVID-19 hastasının tıbbi maske takıp takmadığını giriniz (e/h): ')

#N95 endikasyonu olup olmadığı, yani sağlık çalışanının N95 kullanma gerekliliği olup olmadığı
n95_endikasyonu = input('N95 endikasyonu olup olmadığını giriniz (e/h): ')

#Sağlık çalışanının maske takma durumu
mas_takdimi = input('Sağlık çalışanının maske kullanım durumunu giriniz (t: tıbbi, n: N95, h: hiçbiri): ')

#Sağlık çalışanının göz koruyucu kullanıp kullanmadığı
goz_koruyucu = input('Sağlık çalışanının göz koruyucu kullanıp kullanmadığını giriniz (e/h): ')

#Sağlık çalışanının eldiven/önlük kullanıp kullanmadığı
eldiven_onluk = input('Sağlık çalışanının eldiven&önlük kullanıp kullanmadığını giriniz (e/h): ')

risk_grubu = "risksiz"

if hasta_mas_takdimi == 'e':
    if (n95_endikasyonu == 'e' and mas_takdimi == 't') or (mas_takdimi == 'h'):
        risk_grubu = 'orta'
    elif goz_koruyucu == 'h' or eldiven_onluk == 'h':
        risk_grubu = 'dusuk'

else: #Hasta maske takmazsa
    if mas_takdimi == 'h':
        risk_grubu = 'yuksek'
    elif (n95_endikasyonu == 'e' and mas_takdimi == 't') or (goz_koruyucu == 'h'):
        risk_grubu = 'orta'
    elif eldiven_onluk == 'h':
        risk_grubu = 'dusuk'

if risk_grubu == 'yuksek':
    print('Sağlık çalışanı Yüksek Riskli kategoridedir.\nSemptom gelişmezse 7. günde PCR testi yapılması gereklidir.\nO güne kadar çalışamaz.')

elif risk_grubu == 'orta':
    print('Sağlık çalışanı Orta Riskli kategoridedir.\nSemptom gelişmezse 7. günde PCR testi yapılması gereklidir.\nO güne kadar çalışabilir.')

elif risk_grubu == 'dusuk':
    print('Sağlık çalışanı Düşük Riskli kategoridedir.\nSemptom gelişmezse 7. günde PCR testi yapılması gerekli değildir.\nO güne kadar çalışabilir.')

else:
    print('Sağlık çalışanı Risksiz kategoridedir.')
