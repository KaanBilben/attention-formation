# Objektif 4 — Attention RLModule

| Alan | Değer |
|---|---|
| Objektif | `models/`: değişken boyutlu Agent kümesini işleyen politika ve critic |
| Çıktı | Maskeli attention kodlayıcı + RLlib RLModule (actor + IPPO critic) |
| Bağımlılık | Obj 1-P7 (gözlem sözleşmesi) |
| Açılış | 12.10.2026 |
| Durum | — |

Açık sorular paketi alan geliştiriciye şıklı sorulur (PROJECT.md §6, §11).

---

## İş paketleri

### P1 — Attention kodlayıcı
- **Bağımlılık:** Obj 1-P7
- **Dosyalar:** `models/attention.py`, `tests/models/test_attention.py`, `tests/degismez/test_d3_*.py`, `tests/degismez/test_d4_*.py`
- **Yapılacak:** Agent'ın kendisi + diğer Agent'lar kümesi → sabit boyutlu vektör, maske ile.
- **Kabul kriteri:** `tests/models/test_attention.py`, D-3 ve D-4 testleri yeşil.
- **Açık sorular:** Agent'ın kendisi query mi, self-attention + pooling mi? Boyut, kafa ve katman sayısı?
- **Durum:** —
- **Kontrol eden:** —

### P2 — RLModule
- **Bağımlılık:** P1
- **Dosyalar:** `models/rl_module.py`, `tests/models/test_rl_module.py`
- **Yapılacak:** Kodlayıcı üzerine actor ve critic; RLlib yeni API'sine uygun RLModule.
- **Kabul kriteri:** `tests/models/test_rl_module.py` yeşil (RLlib ile ileri geçiş, aksiyon dağılımı).
- **Açık sorular:** Aksiyon dağılımı (Gauss, tanh ile sıkıştırma)? Actor ve critic kodlayıcıyı paylaşır mı?
- **Durum:** —
- **Kontrol eden:** —

---

## Onay

**Onay:** ⬜ bekliyor

## Kapanış

- [ ] Tüm paketler kabul kriterini karşıladı, farklı ajan kontrol etti
- [ ] `temp/4-*` boşaltıldı
- [ ] CHANGELOG'da sürüm kesildi, tag atıldı
- [ ] TODO durumu `✅`
