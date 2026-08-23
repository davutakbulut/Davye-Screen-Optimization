# Davye Sipariş Yönetim Paneli - Geliştirme ve Senkronizasyon Kuralları

Bu dosya, Davye Sipariş Yönetim Paneli projesinde yapılacak her türlü geliştirme, düzeltme veya yeni özellik talebinde **Antigravity Yapay Zeka Asistanı** tarafından otomatik olarak yüklenen ve harfiyen uygulanması zorunlu ana sistem kuralıdır.

---

## 🛑 1. GELİŞTİRME ÖNCESİ ZORUNLU KONTROL (MANDATORY PRE-CHECK)
Kullanıcıdan herhangi bir sipariş sayfası güncellemesi veya yeni özellik talebi geldiğinde, kod yazmaya başlamadan önce **MUTLAKA** şu kontrol zinciri işletilir:

1. **Daha Önce Yapıldı mı / Nasıl Tasarlandı?**
   * `documantations/index.html` ve hafıza/kurallar taranır.
   * Eğer o alanla ilgili mevcut bir kural, tasarım kararı veya bileşen varsa:
     - **Mevcut Yapıyı Koru:** Daha önce alınmış kararları (örn: flat tasarım, `#ffffff / #f0f6fe` zebra striping, mobilde 3 satır, 3 haneli sipariş no, 4s cache vb.) bozmadan geliştirme yapılır.
     - **Dökümantasyonu Güncelle:** İlgili alan `documantations/index.html` içinde bulunarak yeni mantık ve güncel kod ile revize edilir.
   * Eğer yepyeni bir özellikse:
     - **Yeni Başlık Aç:** `documantations/index.html` sayfasına uygun kategori altında yeni bir bölüm (Section) eklenir.
     - **Sidebar'a Ekle:** Sol sidebar menüsüne yeni başlık ve arama anahtar kelimeleri (`data-keywords`) eklenir.
     - **Gerekçelendir:** "Neden yapıldı?", "Nereden tetikleniyor?", "Tıklanınca ne oluyor?" mantıkları yazılır.

---

## 🏛️ 2. MİMARİ VE TASARIM PRENSİPLERİ (CORE DESIGN PRINCIPLES)

### A. Masaüstü & Mobil Bütünlüğü
1. **Masaüstü (Desktop):**
   * Kapalı kartlar tek satırlık başlıkla gelir ve Cari Adı görünür.
   * Tıklandığında başlıktaki Cari Adı gizlenir ve 4 sütunlu `card-body-grid` açılır (`1.3fr 1.1fr 1.3fr 0.9fr`).
   * Başlıktaki ok 180° döner.
2. **Mobil (Mobile `@media (max-width: 640px)`):**
   * 3 satırlı başlık yapısı (`.row-1`, `.row-2`, `.row-3`) ve buton hiyerarşisi **asla bozulamaz**.
   * Dokunulduğunda dikey tek sütunlu gövde açılır.
   * Sayfa genelinde yatay taşma (`overflow-x`) kesinlikle engellenmelidir (`overflow-x: clip`).

### B. Kart İçi Yükleme (Database Loader) & Cache
1. Bir kart ilk kez tıklandığında 4 saniyelik veritabanı simülasyon loader'ı çalışır (`.order-card.expanded.loading`).
2. Aynı oturumda (sayfa yenilenene kadar) karta tekrar tıklandığında veri önbellekten (`loadedCardsCache = new WeakSet()`) **0ms gecikmeyle anında gelir**.
3. Sayfa yenilendiğinde (F5) önbellek sıfırlanır.

### C. Sipariş Numarası Gösterimi
1. Kart başlığında yalnızca son 3 hane (örn: `007`, `000`, `021`) görünür; başında `...` yer almaz.
2. Tıklandığında veya panoya kopyalandığında sipariş kodunun **tamamı** (`1-WS-2-68007`) kopyalanır.
3. Arama kutusunda hem 3 haneli (`007`) hem de tam kod (`1-WS-2-68007`) ile arama yapılabilir.

### D. Renk Paleti, Zebra Striping & Flat Tasarım
1. Tekil satırlar `#ffffff` (Saf Beyaz), çift satırlar `#f0f6fe` (Pastel Soft Mavi).
2. Kartlarda flat tasarım esastır (`box-shadow: none`).

### E. Doğrulanmış Gerçek Veri Kuralı (Anti-Halüsinasyon)
1. **Depo Kodları:** Yalnızca `MD` (Dental Ürünler) ve `ED` (Ecza Ürünleri) kodları kullanılabilir. Başka hayali depo kodu (MRL, GCL vb.) yazılamaz.
2. **Satış Kanalları:** `TRENDYOL AŞ. ŞTİ.`, `DENTAL PİYASA`, `HEPSİBURADA`, `DAVUT AKBULUT`.
3. **Taşıyıcı Kargo & Teslimat Türleri:** `DHL Kargo (KA)`, `Trendyol Express (KA)`, `HepsiJet (GÖ)`, `Elden Teslim`.

### F. İşlemler Menüsü (8 Aksiyon)
Her kartın işlemler menüsünde şu 8 aksiyon eksiksiz yer alır:
1. `Detaya Git` (Sipariş detay modalını açar)
2. `Müşteri Detay` (Cari CRM modalını açar)
3. `İşlemi Kopyala` (Siparişi klonlar)
4. `Fatura Kes / Görüntüle` (E-Fatura ekranını açar)
5. `İrsaliye Yazdır` (Yazdırma formatı üretir)
6. `Not Ekle` (Kart üstüne sarı acil not barı ekler)
7. `Siparişi İptal Et` (İptal modalı ve gerekçe seçtirir)
8. `Sil` (Listeden animasyonla siler)

### G. Fotoğraflı Paketleme Kontrolü
1. Kamera ikonu yalnızca paketlenmiş veya paketleme masasına girmiş siparişlerde gösterilir (`Paketleme Bekliyor`, `Paketlendi`, `Kargo Bekliyor`, `Kargoda`, `Teslim Edildi`).
2. Taslak, Sipariş Alındı, Hazırlanıyor, İptal ve İade durumlarında kamera ikonu gizlidir.

### H. Sayfalama & Sayaç Düzeni
1. Sayfa başına seçim (`10 Adet ▾`) solda, sayfa numaraları sağda konumlandırılır.
2. Seçicinin hemen yanında `[ 1-10 / 21 ]` kompakt sayaç rozeti yer alır.

---

### I. Müşteri Notu Şeridi (.card-note-bar)
1. Kart kapalıyken de (`.order-card:not(.expanded)`) acil müşteri notunun derhal fark edilebilmesi için `.card-note-bar` **her zaman görünürdür** (`display: flex`).
2. Kapalıyken alt köşeleri yuvarlaktır (`border-radius: 0 0 9px 9px`); kart açıldığında gövdenin üstünde düz şerit olarak kalır (`border-radius: 0`).
3. Tıklandığında veya "Kopyala" butonuna basıldığında not metni panoya kopyalanır.

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
2. Değişiklikler her zaman `git add index.html documantations/index.html GEMINI.md` şeklinde tek bir anlamlı commit ile GitHub `main` dalına pushlanmalıdır.
