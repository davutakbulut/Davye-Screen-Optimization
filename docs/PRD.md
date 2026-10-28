# PRD

## Ne
Davye ERP için sipariş yönetimi ve depo (WMS) toplama arayüzü. Şu an örnek (mock) veriyle çalışan ön yüz prototipi.

## Kimin için
| Kullanıcı | İş |
|---|---|
| Satış / operasyon | Toptan siparişleri listeler, filtreler, sıralar; fiş yazdırır, not ekler, iptal eder |
| Depo personeli | Alınan siparişleri görür, toplamayı başlatır, raf/barkod ile ürün toplar |

## Yapması gerekenler
| Sayfa | İşler |
|---|---|
| `index.html` | Sipariş kartları, durum sekmeleri, 12'li sıralama, gelişmiş filtre, sayfalama, işlemler menüsü (7 aksiyon), modallar, tanıtım turu |
| `alinan-siparisler.html` | Depo sipariş listesi, toplanabilir/toplanamaz/toplanan sekmeleri, "Siparişi Topla / Toplananı Gör" |
| `siparis-toplama.html` | Raf toplama ekranı, barkod okutma, sayılan miktar, tamamlama modalı |
| `documantations/index.html` | Tasarım kurallarının görsel dokümantasyonu |

## Kapsam dışı
- Gerçek veritabanı / backend API: belirlenmedi
- Kullanıcı girişi ve yetkilendirme: belirlenmedi
