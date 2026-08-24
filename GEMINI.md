# Davye Sipariş Yönetim Paneli - Geliştirme ve Senkronizasyon Kuralları

> **Son Sistem Güncellemesi:** 24 / 08 / 2026 03:30  
> Bu dosya, Davye Sipariş Yönetim Paneli projesinde yapılacak her türlü geliştirme, düzeltme veya yeni özellik talebinde **Antigravity Yapay Zeka Asistanı** tarafından otomatik olarak yüklenen ve harfiyen uygulanması zorunlu ana sistem kuralıdır.

---

## 🛑 1. GELİŞTİRME ÖNCESİ ZORUNLU KONTROL (MANDATORY PRE-CHECK)
Kullanıcıdan herhangi bir sipariş sayfası güncellemesi veya yeni özellik talebi geldiğinde, kod yazmaya başlamadan önce **MUTLAKA** şu kontrol zinciri işletilir:

1. **Daha Önce Yapıldı mı / Nasıl Tasarlandı?**
   * `documantations/index.html` ve hafıza/kurallar taranır.
   * Eğer o alanla ilgili mevcut bir kural, tasarım kararı veya bileşen varsa:
     - **Mevcut Yapıyı Koru:** Daha önce alınmış kararları (örn: flat tasarım, `#ffffff / #f0f6fe` zebra striping, mobilde 3 satır, 3 haneli sipariş no, 4s cache, 33ch cari limiti vb.) bozmadan geliştirme yapılır.
     - **Dökümantasyonu Güncelle:** İlgili alan `documantations/index.html` içinde bulunarak yeni mantık ve güncel kod ile revize edilir.
   * Eğer yepyeni bir özellikse:
     - **Yeni Başlık Aç:** `documantations/index.html` sayfasına uygun kategori altında yeni bir bölüm (Section) eklenir.
     - **Sidebar'a Ekle:** Sol sidebar menüsüne yeni başlık ve arama anahtar kelimeleri (`data-keywords`) eklenir.
     - **Gerekçelendir:** "Neden yapıldı?", "Nereden tetikleniyor?", "Tıklanınca ne oluyor?" mantıkları yazılır.
     - **Tarih & Saat Damgası Ekle (Zorunlu):** Eklenen her yeni öğenin veya kuralın ne zaman eklendiği/güncellendiği **`DD / MM / YYYY HH:mm`** formatında hem `GEMINI.md` hem de `documantations/index.html` içerisine kaydedilmelidir.

---

## 🏛️ 2. MİMARİ VE TASARIM PRENSİPLERİ (CORE DESIGN PRINCIPLES)

### A. Masaüstü & Mobil Bütünlüğü
1. **Masaüstü (Desktop):**
   * Üst header (`.davye-top-header`) ve sol sidebar menü (`.app-sidebar`) ekran kaydırıldığında **daima sabit (fixed)** kalır; sağdaki sipariş listesi (`.app-main-content`) bağımsız olarak kayar.
   * Kapalı kartlar tek satırlık başlıkla gelir ve Cari Adı görünür.
   * Tıklandığında başlıktaki Cari Adı gizlenir ve 4 sütunlu `card-body-grid` açılır (`1.3fr 1.1fr 1.3fr 0.9fr`).
   * Başlıktaki ok 180° döner.
2. **Mobil (Mobile `@media (max-width: 640px)`):**
   * Üst header (`.davye-top-header`) mobilde de sayfa kaydırıldığında **en üstte sabit (fixed)** kalır.
   * 3 satırlı başlık yapısı (`.row-1`, `.row-2`, `.row-3`) ve buton hiyerarşisi **asla bozulamaz**.
   * Dokunulduğunda dikey tek sütunlu gövde açılır.
   * Sayfa genelinde yatay taşma (`overflow-x`) kesinlikle engellenmelidir (`overflow-x: clip`).

### B. Kart İçi Yükleme (Database Loader) & Cache
1. Bir kart ilk kez tıklandığında 4 saniyelik veritabanı simülasyon loader'ı çalışır (`.order-card.expanded.loading`).
2. Aynı oturumda (sayfa yenilenene kadar) karta tekrar tıklandığında veri önbellekten (`loadedCardsCache = new WeakSet()`) **0ms gecikmeyle anında gelir**.
3. Sayfa yenilendiğinde (F5) önbellek sıfırlanır.

### C. Sipariş Numarası Gösterimi & Sıralama
1. Kart başlığında son 3 hane (örn: `898`, `897`, `896` ... `878`) görünür; başında `...` yer almaz.
2. Sipariş kodunun tamamı sonu 5 haneli sayı olacak biçimde **`1-WS-2-51898`** formatındadır ve listede büyükten küçüğe doğru (`51898`'den `51878`'e) ardışık olarak sıralanır.
3. Tıklandığında veya panoya kopyalandığında sipariş kodunun **tamamı** (`1-WS-2-51898`) kopyalanır.
4. Arama kutusunda hem 3 haneli (`898`) hem de tam kod (`1-WS-2-51898`) ile arama yapılabilir.

### D. Renk Paleti, Zebra Striping & Flat Tasarım
1. Tekil satırlar `#ffffff` (Saf Beyaz), çift satırlar `#f0f6fe` (Pastel Soft Mavi).
2. Kartlarda flat tasarım esastır (`box-shadow: none`).

### E. Doğrulanmış Gerçek Veri Kuralı (Anti-Halüsinasyon)
1. **Depo Kodları:** Yalnızca `MD` (Dental Ürünler) ve `ED` (Ecza Ürünleri) kodları kullanılabilir. Başka hayali depo kodu (MRL, GCL vb.) yazılamaz.
2. **Satış Kanalları:** `DAVUT AKBULUT`, `ÜMİT VELİOĞLU`, `ERDİ EKİZ`, `MERKEZ DEPO`, `TRENDYOL AŞ. ŞTİ.`, `DENTAL PİYASA`, `HEPSİBURADA`.
3. **Taşıyıcı Kargo & Teslimat Türleri:** `DHL Kargo (KA)`, `Trendyol Express (KA)`, `HepsiJet (GÖ)`, `Elden Teslim`.

### F. İşlemler Menüsü (6 Aksiyon)
Her kartın işlemler menüsünde şu 6 aksiyon eksiksiz yer alır:
1. `Detaya Git` (Sipariş detay modalını açar)
2. `Müşteri Detay` (Cari CRM modalını açar)
3. `İşlemi Kopyala` (Siparişi klonlar)
4. `Not Ekle` (Kart üstüne sarı acil not barı ekler)
5. `Siparişi İptal Et` (İptal modalı ve gerekçe seçtirir)
6. `Sil` (Listeden animasyonla siler)

### G. Fotoğraflı Paketleme Kontrolü
1. Kamera ikonu yalnızca paketlenmiş veya paketleme masasına girmiş siparişlerde gösterilir (`Paketleme Bekliyor`, `Paketlendi`, `Kargo Bekliyor`, `Kargoda`, `Teslim Edildi`).
2. Taslak, Sipariş Alındı, Hazırlanıyor, İptal ve İade durumlarında kamera ikonu gizlidir.

### H. Sayfalama & Sayaç Düzeni
1. Sayfa başına seçim (`10 Adet ▾`) solda, sayfa numaraları sağda konumlandırılır.
2. Seçicinin hemen yanında `1-10 / 21` sayaç metni yer alır (arka plansız ve çerçevesiz düz yazı formatında).

---

### I. Müşteri Notu Şeridi (.card-note-bar)
1. Kart kapalıyken de (`.order-card:not(.expanded)`) acil müşteri notunun derhal fark edilebilmesi için `.card-note-bar` **her zaman görünürdür** (`display: flex`).
2. Kapalıyken alt köşeleri yuvarlaktır (`border-radius: 0 0 9px 9px`); kart açıldığında gövdenin üstünde düz şerit olarak kalır (`border-radius: 0`).
3. Tıklandığında veya "Kopyala" butonuna basıldığında not metni panoya kopyalanır.

---

### J. Tarih Formatı Standartı (DD / MM / YYYY)
1. Kart başlığında, detay modallarında, kargo çizelgesinde ve sistem genelinde tüm tarihler tire yerine boşluklu eğik çizgi ile **`DD / MM / YYYY`** (örn: `21 / 08 / 2026`) formatında gösterilir.
2. Vade tarihleri ve sipariş oluşturma tarihleri bu formatla tam uyumludur.

---

### K. Cari İsimleri Karakter Sınırı ve Yatay Kaydırma (33ch) & Sabit İkon
1. Kart başlığında (`.header-cari-name span:first-of-type`) ve gövde 1. sütunundaki (`.cari-name .cari-title-left`) cari/müşteri ünvanları `max-width: 33ch` ile sınırlandırılır (`GÜLÜŞ AĞIZ VE DİŞ SAĞLIĞI POLİKLİ` referans genişliği).
2. 33 karakterden uzun ünvanlar kart düzenini bozmaz veya alt satıra taşmaz; `overflow-x: auto; scrollbar-width: none;` sayesinde yatayda kaydırılabilir.
3. Cari adının solundaki ikon (Bina/Klinik/Şahıs `svg`), metin ne kadar uzun olursa olsun **asla kaybolmaz veya daralmaz** (`flex-shrink: 0 !important; min-width: 12px; display: inline-block;`).

---

### L. Kısmi Ödeme Tutar Gösterimi (Siyah / Kırmızı)
1. Kısmi ödeme yapılmış siparişlerde tutar alanı hem başlıkta hem de finansal özet sütununda `[Toplam Tutar ₺] / [Kalan Ödenmemiş Tutar ₺]` formatında gösterilir (örn: `1.920,00 ₺ / 920,00 ₺` veya `12.500,00 ₺ / 7.500,00 ₺`).
2. Soldaki toplam sipariş tutarı **Siyah** (`.price-total` - `#0f172a`), ayırıcı eğik çizgi **Gri** (`.price-divider` - `#94a3b8`), sağdaki ödenmemiş kalan tutar ise **Kırmızı** (`.price-remaining` - `#dc2626`) olarak vurgulanır.
3. Ödeme durumu rozeti `pay-partial` (`Kısmi Ödendi`) sarı/amber tonlarında gösterilir.

---

### M. 12'li Hızlı Sıralama Çubuğu ve 3-Kademeli Tıklama Döngüsü (.inline-sort-bar-wrapper)
1. `top-toolbar` ve `status-filters` alanlarının hemen altında, açılır dropdown yerine yan yana duran yatayda kaydırılabilir **12 adet sıralama chipleri** yer alır (`Sipariş No`, `Tarih`, `Cari`, `Tutar`, `Kalan Tutar`, `Vade`, `Ürün Adedi`, `Toplanan`, `Depo`, `Satış Kanalı`, `Fatura Durumu`, `Teslimat Türü`).
2. **3-Kademeli Döngü Mantığı (3-State Cycle):**
   - **Başlangıç / Nötr (State 0):** Yatay çift ok (`⇄` - `SORT_SVG_ICONS.neutral`).
   - **1. Tıklama (State 1):** Büyükten Küçüğe / Azalan / En Yeni (Aşağı Ok `↓` - `.active-desc`).
   - **2. Tıklama (State 2):** Küçükten Büyüğe / Artan / En Eski (Yukarı Ok `↑` - `.active-asc`).
   - **3. Tıklama (State 0):** Sıralama sıfırlanır ve varsayılan sıralamaya (`51898`'den `51878`'e) geri döner.
3. Başka bir chip tıklandığında önceki aktif chip derhal nötr duruma (`⇄`) döner ve yeni chip 1. tıklama (State 1) ile başlar.
4. Sıralama yapıldığında sayfalama (`paginationBar`) daima listenin en altında kalır ve sayfa numarası `1`'e alınarak güncellenir.

---

### N. Pazaryeri Siparişleri Etiketleme & "Pazaryerleri Gizli" Filtresi (.marketplace-toggle-label)
1. Satış kanalı `TRENDYOL AŞ. ŞTİ.` veya `HEPSİBURADA` olan siparişler DOM'da `data-order-group="Pazaryeri Siparişleri"` ve `data-is-marketplace="true"` olarak etiketlenir (`ordersDatabase` içinde `orderGroup: "Pazaryeri Siparişleri"`, `isMarketplace: true`).
2. Üst toolbar filtre alanında `#btnAdvToggle` butonunun yanında varsayılan olarak **seçili (`checked: true`)** gelen `Pazaryerleri Gizli` onay kutusu (`#hideMarketplaceCheck`) yer alır.
3. Onay kutusu işaretliyken pazaryeri siparişleri gizlenir ve sayfalama ile durum sekmeleri yalnızca direkt siparişleri sayar/gösterir.
4. Tik kaldırıldığında (`checked: false`), pazaryeri siparişleri listede orijinal kronolojik/sıralı yerlerine derhal geri döner ve sayaçlar güncellenir.

---

## 📖 3. DÖKÜMANTASYON SAYFASI KURALLARI (`documantations/index.html`)
1. **Sabit Header (Fixed):** Üst başlık hem masaüstünde hem mobilde `position: fixed` olarak en üstte sabit kalır.
2. **Masaüstü Sticky Sidebar:** Sol menü `position: sticky; top: 78px; align-self: flex-start;` ile masaüstünde kaydırma boyunca sabit kalır.
3. **Mobilde Drawer (Off-Canvas):** Mobilde içerik tam ekran açılır; logoya tıklandığında sol menü soldan açılır ve bir başlık seçildiğinde kendiliğinden kapanır.
4. **Yüksek Performanslı ScrollSpy:** Tarayıcıyı kasmayan donanım hızlandırmalı `IntersectionObserver` ile sağdaki içerik kaydıkça sol menü otomatik seçilir.
5. **Canlı UI Örnekleri:** Her bölümün altında teorik anlatımın yanında birebir çalışan, interaktif canlı HTML/CSS bileşeni yer almalıdır.

---

## 🔄 4. OTOMATİK DÖKÜMANTASYON SENKRONİZASYONU (DOCS SYNC)
1. Her kod değişikliğinde `index.html` ve `documantations/index.html` eşzamanlı olarak güncellenmelidir.
2. Eklenen veya güncellenen her kural/özellik için en son güncellenme tarih ve saati (`DD / MM / YYYY HH:mm`) `GEMINI.md` ve dökümantasyona işlenmelidir.
3. Değişiklikler her zaman `git add index.html documantations/index.html GEMINI.md` şeklinde tek bir anlamlı commit ile GitHub `main` dalına pushlanmalıdır.
