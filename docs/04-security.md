# Güvenlik

## Anahtar ve gizli bilgi
- Token / şifre dosyaya, commit'e, sohbet çıktısına yazılmaz.
- **Açık sorun:** `.git/config` içindeki `origin` adresine gömülü (geçersiz) bir GitHub token'ı var. Adres token'sız hale getirilmeli; push `gh auth` kimliğiyle yapılır.

## Yetki
- Kullanıcı girişi / rol: belirlenmedi (prototip).
- `server.py` yalnız `127.0.0.1`'e bağlanır; dışarıya açılmamalıdır.

## Kullanıcı girdisi
- `POST /api/save-content` kimlik doğrulaması olmadan `index.html`'i yeniden yazabilir ve git'e push eder; `Access-Control-Allow-Origin: *` döner. Sunucu herkese açık bir ağda çalıştırılmamalıdır.
- Arayüzdeki satır içi düzenleme metni HTML'e yazılır; kaçış (escape) kuralı: belirlenmedi.

## Kişisel veri
- Sayfalardaki müşteri adı, VKN, telefon, adres verileri örnek (mock) veridir. Gerçek müşteri verisi repoya konmaz.
