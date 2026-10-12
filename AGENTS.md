# AGENTS.md

**Tüm çalışma kuralları, komutlar ve mimari [PROJECT.md](PROJECT.md) dosyasındadır.** Oturum başında baştan sona oku. Kural burada tekrarlanmaz.

## Rolün: geliştirici (Codex / OpenCode)

Sana verilen iş paketini uygularsın. Paket tanımı ve kabul kriteri `docs/plan/` altındaki plan dosyasındadır.

## Oturum başı

1. [PROJECT.md](PROJECT.md): tamamı
2. [GLOSSARY.md](GLOSSARY.md): terimler
3. `docs/plan/<obj-no>-*.md`: senin paketin, bağımlılığı, kabul kriteri

## Durman gereken yerler

- Paketin kabul kriteri yoksa başlama, iste (§7a).
- Paketin bağımlılığı bitmemişse başlama.
- Paketin nasıl yapılacağı yazmıyorsa varsayma; şıklı sor, önerdiğin cevap ilk şık olsun (§11).
- İş kapsam dışına çıkıyorsa kod yazma, bildir (§2).
- Başkasının aldığı pakette kod yazma; sorunu not olarak bırak (§4).
- Değişmezler pazarlık dışı (§3).

## Unutma

- Test önce: davranışa göre yaz, **kırmızı gör**, sonra kod (§7).
- `tests/degismez/` altındaki testler silinmez, zayıflatılmaz (§3).
- Deneme `temp/<obj-no>-<konu>/` altında, `NOT.md` ile (§5).
- Branch `obj-<no>-p<paket>`, commit `[obj-no] açıklama (@ajan)` (§9).
- İş bitince CHANGELOG + paket durumu (§8).
- Kendi işini sen onaylamazsın (§7b).
