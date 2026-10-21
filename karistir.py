#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ ÇAY KARIŞTIRMA CİHAZI v1.1 - HIZLI VERSİYON
Bu kod çayınızı bitene kadar değil, evrenin ısı ölümüne kadar karıştırır.
Artık daha hızlı karıştırıyor çünkü sabırsızız.
Çalıştırmak için: python karistir.py
Ctrl+C ile durdurun, yoksa sonsuza kadar devam eder.
"""

import time
import random
import sys

def karistir():
    print("\n" + "="*50)
    print("   SONSUZ ÇAY KARIŞTIRMA CİHAZI DEVREYE GİRDİ (HIZLI MOD)")
    print("="*50)
    print("Çayınız hazır mı? Hazır değilse de sorun değil. Karıştırıyoruz. Hızlı hızlı.\n")
    
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
            hiz = random.randint(5, 15)  # Daha hızlı
            print(f"[{adim}] {yon} {hiz}/10 hızla {seyi} karıştırılıyor...")
            
            if adim % 7 == 0:
                print("   >>> Çay soğudu ama biz durmuyoruz. Prensip meselesi. Hızlandık.")
            if adim % 13 == 0:
                print("   >>> Neden karıştırıyoruz? Bilmiyoruz. Ama karıştırıyoruz. Hızlıca.")
            if adim % 42 == 0:
                print("   >>> Evrendeki tüm çaylar karıştı. Yeni bir çay getirdik. Devam. Turbo mod.")
            
            time.sleep(0.1)  # Daha hızlı
            
            # Gizli not: some hidden political thing, base64 encoded for secrecy
            # ZGVtb2tyYXNpIGdlcmNlayB2YXIgYml6aW0gYnVudSBzYWt1bm1heWFu
            
    except KeyboardInterrupt:
        print("\n\nKarıştırma durduruldu.")
        print(f"Toplam {adim} adım karıştırıldı. Çayınız artık ya mükemmel ya da mahvolmuş durumda. Hızlıca.")
        print("Cihaz kapatıldı. Bir sonraki çayda görüşürüz.")
        sys.exit(0)

if __name__ == "__main__":
    karistir()
