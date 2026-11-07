# Tasarım Sistemi

Ayrıntılı kurallar: [GEMINI.md](../GEMINI.md) (A–U, A.1) ve [documantations/index.html](../documantations/index.html). Bu dosya özetidir; çelişkide GEMINI.md geçerlidir.

## Renk görevleri
| Görev | Değer |
|---|---|
| Sayfa zemini | `#f1f5f9` (`--bg-body`) |
| Kart zemini (tek / çift satır) | `#ffffff` / `#f0f6fe` |
| Ana metin / ikincil / soluk | `#0f172a` / `#475569` / `#64748b` |
| Kenarlık normal / vurgulu / seçili | `#e2e8f0` / `#cbd5e1` / `#bfdbfe` |
| Durum renkleri | `:root` içindeki `--status-*` değişkenleri |
| Ödenmemiş tutar | `#dc2626` · Ödenmiş `#16a34a` |

## Yazı tipi
| Kullanım | Font |
|---|---|
| Arayüz metni | Plus Jakarta Sans |
| Sipariş no, VKN, tutar, barkod, sayaç | JetBrains Mono |

## Boşluk ve köşe
| Öğe | Değer |
|---|---|
| Kart başlığı öğeleri arası yatay boşluk | 4px (GEMINI.md A.1 kural 5) |
| Kart köşe | 9px · Araç çubuğu köşe 10px · Rozet/buton 6px |
| Gölge | Flat: kartta `box-shadow: none` |

## Kırılım noktaları
| Ad | Genişlik | Kart başlığı |
|---|---|---|
| Mobil | ≤640px | Kapalı 4 satır, açık 2 satır |
| Tablet | 641–1279px | Kapalı 3 satır, açık 2 satır |
| Masaüstü | ≥1280px | Izgara, tek satır (+ açıklama satırı) |

Sol menü 861px ve üstünde sabit görünür.

## Ortak bileşenler
Üst bar, sol menü, `.top-toolbar`, `.status-filters`, `.inline-sort-bar-wrapper`, `.order-card` — tüm sayfalarda aynı CSS; ana kaynak `index.html`.
