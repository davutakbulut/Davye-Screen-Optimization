# CLAUDE.md — Davye Sipariş Yönetim Paneli

## Başlamadan önce oku
1. Bu dosya
2. [GEMINI.md](GEMINI.md) — tasarım ve davranış kuralları (A–U, A.1 responsive kural seti). **Asıl kural kaynağı budur.**
3. İşin dokunduğu belge: [PRD](docs/01-product-requirements.md) · [Mimari](docs/02-architecture.md) · [Tasarım sistemi](docs/03-design-system.md) · [Güvenlik](docs/04-security.md) · [Kod stili](docs/05-code-style.md) · [Test](docs/06-testing-and-release.md)

## Genel kurallar
- Her düzenlemeden sonra commit + `main`'e push (geri dönülebilirlik). Commit mesajı: Türkçe, `feat:/fix:/refactor:/docs:` önekli.
- Kart başlığı / ortak bileşen değişikliği GEMINI.md A.1'e uyar; ortak bileşenlerde ana kaynak `index.html`, diğer sayfalara aynen kopyalanır.
- Mimari, tasarım, güvenlik veya test düzeni değişirse ilgili `docs/` belgesi aynı commit'te güncellenir.

## Dokunulmaz kurallar
- Gerçek veri uydurulmaz (GEMINI.md E).
- Tek `<script>` bloğu + `window.*` export düzeni bozulmaz (GEMINI.md T).
- Hiçbir genişlikte yatay taşma olmaz.
- Token / şifre dosyaya, commit'e veya URL'ye yazılmaz.

## Yararlı komutlar
| İş | Komut |
|---|---|
| Sunucuyu başlat | `python3 server.py` → http://localhost:8888/index.html |
| Sayfalar | `index.html` · `alinan-siparisler.html` · `siparis-toplama.html` · `documantations/index.html` |
| Kod grafiği | `/graphify .` (çıktı: `graphify-out/`) |
