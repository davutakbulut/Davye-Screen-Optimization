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
1. **Masaüstü & Mobil Bütünlüğü:**
   * Masaüstünde kapalı kartlar tek satırlık başlıkla gelir; tıklandığında 4 sütunlu `card-body-grid` açılır ve başlıktaki Cari Adı gizlenir.
   * Mobildeki (`@media (max-width: 640px)`) 3 satırlı başlık yapısı ve buton hiyerarşisi **asla bozulamaz**.
   * HTML manipülasyonu yapılırken regex ile toplu silme yapılmamalı; CSS Grid/Flex kuralları tercih edilmelidir.
2. **Kart İçi Yükleme (Database Loader) & Cache:**
   * Bir kart ilk kez tıklandığında 4 saniyelik veritabanı simülasyon loader'ı çalışır (`.order-card.expanded.loading`).
   * Aynı oturumda (sayfa yenilenene kadar) karta tekrar tıklandığında veri önbellekten (`loadedCardsCache`) 0ms gecikmeyle anında gelir.
3. **Sipariş Numarası Gösterimi:**
   * Kart başlığında yalnızca son 3 hane (örn: `007`, `000`, `021`) görünür.
   * Tıklandığında veya panoya kopyalandığında sipariş kodunun **tamamı** (`1-WS-2-68007`) kopyalanır.
4. **Zebra Striping & Gölgelendirme:**
   * Tekil satırlar `#ffffff`, çift satırlar `#f0f6fe`.
   * Kartlarda flat tasarım esastır (`box-shadow: none`).
5. **Doğrulanmış Gerçek Veri Kuralı (Anti-Halüsinasyon):**
   * Dökümantasyona `index.html` dosyasında yer almayan hiçbir uydurma veri, hayali depo kodu veya hayali kanal yazılamaz. Depo kodları yalnızca `MD` ve `ED`'dir.

---

## 🔄 3. OTOMATİK DÖKÜMANTASYON SENKRONİZASYONU (DOCS SYNC)
1. Her kod değişikliğinde `index.html` ve `documantations/index.html` eşzamanlı olarak güncellenmelidir.
2. Değişiklikler her zaman `git add index.html documantations/index.html GEMINI.md` şeklinde tek bir anlamlı commit ile GitHub `main` dalına pushlanmalıdır.
