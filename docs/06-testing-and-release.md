# Test

## Test türleri
| Tür | Durum |
|---|---|
| Birim / otomatik test | Yok (belirlenmedi) |
| Görsel / düzen doğrulaması | Tarayıcıda genişlik emülasyonu + JS ile ölçüm (öğe satırı, kenar hizası, 4px boşluk, taşma) |

## Komutlar
```bash
python3 server.py   # sonra sayfaları tarayıcıda aç
```

## Test verisi kuralı
- Yalnız sayfa içindeki örnek veriler kullanılır; gerçek müşteri verisi eklenmez.

## Yayından önce kontrol listesi
- [ ] Değişen bileşen şu genişliklerde kapalı ve açık kartla ölçüldü: 320, 375, 660, 768, 1024, 1279, 1280, 1440 px (GEMINI.md A.1 kural 8)
- [ ] Hiçbir genişlikte yatay taşma yok
- [ ] Ortak bileşen değiştiyse diğer sayfalarda da aynı konumda (A.1 kural 9)
- [ ] Konsolda hata yok
- [ ] Commit + push yapıldı
