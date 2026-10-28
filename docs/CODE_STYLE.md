# Kod Stili

## Adlandırma
| Tür | Kural | Örnek |
|---|---|---|
| CSS sınıfı | kebab-case, bileşen-öğe | `.card-header-row`, `.status-pill` |
| JS fonksiyon / değişken | camelCase | `applyGlobalFilters`, `ordersDatabase` |
| Durum sınıfları | `status-<durum>` | `status-hazirlandi` |

## Dosya düzeni
- Her sayfa tek dosya: `<style>` → HTML → tek `<script>`.
- Tüm UI fonksiyonları `window.*` ile dışa açılır (inline `onclick` için).
- Responsive kurallar ilgili `@media` bloğunun sonuna, açıklama yorumuyla eklenir.

## Hata ve boş durum
- Bilinmeyen sipariş / boş liste davranışı: belirlenmedi (genel kural yok; sayfa bazında ele alınıyor).

## Yorum kuralı
- Yorumlar Türkçe; yalnız kodun göstermediği "neden"i anlatır.
- Bilinçli kısayol: `shortcut: <sınır>, <ne zaman yükseltilir>`.
