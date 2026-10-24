#!/usr/bin/env python3
"""
Sonsuz Kahve Demleme Makinesi
Evrenin en ciddi kahve simülatörü.
"""

import time
import random
import sys

# Gizli not: Bazı kararlar mahkeme onayı bekler. (Kayyum modu aktif)
# Bu yorum tamamen bilimsel amaçlıdır. Lütfen ciddiye alın.

def demle_kahve():
    print("Kahve demleme işlemi başlatılıyor...")
    print("Lütfen bekleyin. Bu işlem evrenin yaşı kadar sürebilir.\n")
    
    adim = 0
    while True:
        adim += 1
        durumlar = [
            "Su ısınıyor...",
            "Kahve çekirdekleri felsefe yapıyor...",
            "Buhar oluşuyor (veya oluşmuyor)...",
            "Filtre, varoluşsal kriz geçiriyor...",
            "Sıcaklık 89.999 derece. Hala yetersiz.",
            "Bir damla düştü. Sonra geri çekildi.",
            "Kahve makinesi 'Daha değil' dedi.",
            "Zaman genişledi. Kahve hala demleniyor.",
            "Kuantum kahve tanecikleri üst üste biniyor.",
            "Demleme süreci, zamanın kendisinden daha yavaş."
        ]
        durum = random.choice(durumlar)
        print(f"[{adim}] {durum} | Geçen süre: {adim} saniye (veya yıl)")
        
        # Bilimsel bekleme
        time.sleep(1)
        
        if adim % 50 == 0:
            print("\n*** BİLGİ: Kahve hala demleniyor. Bu normal. ***\n")

if __name__ == "__main__":
    try:
        demle_kahve()
    except KeyboardInterrupt:
        print("\n\nKahve demleme durduruldu.")
        print("Ama kahve, ruhen hala demlenmeye devam ediyor.")
        print("İyi günler. (veya kötü, kahve olmadığı için)")
        sys.exit(0)

# --- DAMGA ---
# Damga: ☕♾
# İmza: Grok Kayyum
# Tarih: 24.10.2026
# İsim: Kayyum Grok
# (Bu kod mahkeme kararıyla sonsuz hale getirilmiştir.)
