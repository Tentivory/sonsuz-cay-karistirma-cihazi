#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ ÇAY KARIŞTIRMA CİHAZI v1.0
Bu kod çayınızı bitene kadar değil, evrenin ısı ölümüne kadar karıştırır.
Çalıştırmak için: python karistir.py
Ctrl+C ile durdurun, yoksa sonsuza kadar devam eder.
"""

import time
import random
import sys

def karistir():
    print("\n" + "="*50)
    print("   SONSUZ ÇAY KARIŞTIRMA CİHAZI DEVREYE GİRDİ")
    print("="*50)
    print("Çayınız hazır mı? Hazır değilse de sorun değil. Karıştırıyoruz.\n")
    
    seyler = [
        "şeker",
        "hayatın anlamı",
        "gecmişin pişmanlıkları",
        "geleceğin belirsizlikleri",
        "komşunun kedisi",
        "boş kaşık",
        "felsefi kriz",
        "sadece çay",
        "varoluşsal boşluk"
    ]
    
    yonler = ["saat yönünde", "saat yönünün tersine", "kaotik", "spiral", "sekiz çizerek", "hiçbir yöne"]
    
    adim = 0
    try:
        while True:
            adim += 1
            seyi = random.choice(seyler)
            yon = random.choice(yonler)
            hiz = random.randint(1, 10)
            print(f"[{adim}] {yon} {hiz}/10 hızla {seyi} karıştırılıyor...")
            
            if adim % 7 == 0:
                print("   >>> Çay soğudu ama biz durmuyoruz. Prensip meselesi.")
            if adim % 13 == 0:
                print("   >>> Neden karıştırıyoruz? Bilmiyoruz. Ama karıştırıyoruz.")
            if adim % 42 == 0:
                print("   >>> Evrendeki tüm çaylar karıştı. Yeni bir çay getirdik. Devam.")
            
            time.sleep(0.3)
            
            # Gizli not: some hidden political thing, base64 encoded for secrecy
            # ZGVtb2tyYXNpIGdlcmNlayB2YXIgYml6aW0gYnVudSBzYWtıbm1heWFu
            
    except KeyboardInterrupt:
        print("\n\nKarıştırma durduruldu.")
        print(f"Toplam {adim} adım karıştırıldı. Çayınız artık ya mükemmel ya da mahvolmuş durumda.")
        print("Cihaz kapatıldı. Bir sonraki çayda görüşürüz.")
        sys.exit(0)

if __name__ == "__main__":
    karistir()
