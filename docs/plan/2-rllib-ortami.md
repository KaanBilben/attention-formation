# Objektif 2 — RLlib ortamı (Faz 1)

| Alan | Değer |
|---|---|
| Objektif | `env/`: `sim/`'i RLlib `MultiAgentEnv` olarak sarmak |
| Çıktı | Faz 1 ortamı: rastgele doğma, başarıda `terminated`, T adımda `truncated` |
| Bağımlılık | Obj 1 |
| Açılış | 12.10.2026 |
| Durum | — |

Açık sorular paketi alan geliştiriciye şıklı sorulur (PROJECT.md §6, §11).

---

## İş paketleri

### P1 — Faz 1 MultiAgentEnv
- **Bağımlılık:** Obj 1 (P1–P7)
- **Dosyalar:** `env/formation_env.py`, `tests/env/test_formation_env.py`
- **Yapılacak:** reset (N seçimi, rastgele doğma), step (aksiyon → sim → gözlem/ödül), sonlanma.
- **Kabul kriteri:** `tests/env/test_formation_env.py` yeşil: RLlib ortam kontrolü geçiyor, rastgele aksiyonla 1000 episode hatasız.
- **Açık sorular:** Doğma bölgesi ve dağılımı? Episode başında N nasıl seçilir? Başarıda tüm Agent'lar mı biter? Ortam config'i nereden gelir?
- **Durum:** —
- **Kontrol eden:** —

---

## Onay

**Onay:** ⬜ bekliyor

## Kapanış

- [ ] Kabul kriteri karşılandı, farklı ajan kontrol etti
- [ ] `temp/2-*` boşaltıldı
- [ ] CHANGELOG'da sürüm kesildi, tag atıldı
- [ ] TODO durumu `✅`
