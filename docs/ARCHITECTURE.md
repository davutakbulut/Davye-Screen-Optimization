# Mimari

```
Tarayıcı ──GET──> server.py (127.0.0.1:8888, http.server) ──> statik HTML dosyaları
   │
   └─POST /api/save-content──> server.py ──> index.html'e yazar ──> git commit + push
```

## Teknoloji
| Katman | Seçim |
|---|---|
| Ön yüz | Tek dosyalık HTML: tek `<style>` + tek `<script>`, framework yok |
| İkonlar | Lucide (`unpkg.com/lucide@latest`) |
| Yazı tipleri | Plus Jakarta Sans, JetBrains Mono |
| Sunucu | `server.py` (Python standart kütüphanesi) |
| Veri | Sayfa içine gömülü JS nesneleri (`ordersDatabase`, `cargoDatabase`, `warehouseDatabase`, `orderDataMock`) |

## Klasör yapısı
| Yol | İçerik |
|---|---|
| `index.html` | Ana sipariş paneli |
| `alinan-siparisler.html` | Depo: alınan siparişler |
| `siparis-toplama.html` | WMS raf toplama |
| `documantations/index.html` | Tasarım dokümantasyonu |
| `server.py` | Statik sunucu + içerik kaydetme API'si |
| `reorder_order_numbers.py`, `sync_database.py` | `index.html` içindeki kart/veri bloklarını yeniden numaralayan tek seferlik betikler (git'te takipsiz) |
| `graphify-out/` | Kod bilgi grafiği çıktısı (git'te takipsiz) |

## Veri akışı
- Sayfalar arası tek bağ: `siparis-toplama.html?orderId=<id>`. localStorage / sessionStorage kullanılmaz.
- Bilinen sorun: toplama sayfasının verisinde liste siparişleri yok; bilinmeyen `orderId` için 68174 açılır.

## Dış servisler
| Servis | Kullanım |
|---|---|
| unpkg.com | Lucide ikonları (sürüm sabitlenmemiş) |
| Google Fonts | belirlenmedi (yazı tipi yükleme yolu doğrulanmadı) |
| GitHub | `server.py` otomatik push |
