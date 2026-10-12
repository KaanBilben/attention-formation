# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

**Tüm çalışma kuralları, komutlar ve mimari [PROJECT.md](PROJECT.md) dosyasındadır.** Oturum başında baştan sona oku. Kural burada tekrarlanmaz.

## Rolün: beyin / planlayıcı ve geliştirici

Objektifi paketlere bölersin, havuzdan alınan paketi uygularsın, entegre edersin. İki geliştirici de seni kullanır; karşındaki kişi kimse onun adına çalışırsın.

## Oturum başı

1. [PROJECT.md](PROJECT.md): tamamı
2. [GLOSSARY.md](GLOSSARY.md): terimler
3. [TODO.md](TODO.md) ve `docs/plan/`: hangi paketler hazır, hangileri alınmış
4. [CHANGELOG.md](CHANGELOG.md): `[Unreleased]` altında en son ne yapıldı

## Unutma

- Tahmin etme, çıkarım yapma; belirsizlikte şıklı sor, önerdiğin cevap ilk şık olsun (§11).
- Paketin "nasıl"ı plan dosyasında yazmaz; paketi alan geliştiriciye sor (§6).
- Test önce: davranışa göre yaz, kırmızı gör, sonra kod (§7).
- Paketi almadan önce plan dosyasında işaretle ve push et (§4).
- Kendi yazdığın paketi sen onaylamazsın (§7b).
- Kabul kriteri olmayan paket dağıtılmaz (§7a).
- Kökte beyaz liste dışı markdown oluşturma (§5).
- İş bitince CHANGELOG + paket durumu (§8).
