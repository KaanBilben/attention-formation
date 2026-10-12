# Objektif 5 — Faz 1 eğitimi

| Alan | Değer |
|---|---|
| Objektif | `training/`: PPO ile Faz 1 eğitimi ve müfredat |
| Çıktı | N ≤ 8 için başarı oranı ≥ %80 olan checkpoint, izleyicide oynatılıyor |
| Bağımlılık | Obj 2, 3, 4 |
| Açılış | 12.10.2026 |
| Durum | — |

Açık sorular paketi alan geliştiriciye şıklı sorulur (PROJECT.md §6, §11).

---

## İş paketleri

P1 ve P3 paralel; P2, P1'i bekler.

### P1 — Sabit N=4 eğitimi
- **Bağımlılık:** Obj 2, Obj 4
- **Dosyalar:** `training/train.py`, `tests/training/test_train.py`
- **Yapılacak:** RLlib PPO, tüm Agent'lar tek policy'ye bağlı; checkpoint ve TensorBoard logu. Öğrenmenin temelde çalıştığını müfredatsız göstermek.
- **Kabul kriteri:** `tests/training/test_train.py` yeşil (kısa eğitim hatasız, checkpoint üretiyor); N=4 eğitiminde başarı oranı artıyor (log kanıtı plan dosyasına).
- **Açık sorular:** PPO hiperparametreleri? Durdurma kriteri? Log ve checkpoint nereye?
- **Durum:** —
- **Kontrol eden:** —

### P2 — Müfredat
- **Bağımlılık:** P1
- **Dosyalar:** `training/curriculum.py`, `tests/training/test_curriculum.py`
- **Yapılacak:** Son K episode'da başarı ≥ %80 olunca N_max artar, 1 → 8.
- **Kabul kriteri:** `tests/training/test_curriculum.py` yeşil; tam eğitimde N ≤ 8 için başarı ≥ %80 (kanıt plan dosyasına).
- **Açık sorular:** K? Artış adımı? Başarı oranı nasıl ölçülür?
- **Durum:** —
- **Kontrol eden:** —

### P3 — Checkpoint oynatma
- **Bağımlılık:** Obj 3-P1, Obj 4-P2
- **Dosyalar:** `viewer/policy_runner.py`, `tests/viewer/test_policy_runner.py`
- **Yapılacak:** İzleyicide checkpoint yükleyip Agent'ları eğitilmiş politikayla sürmek; N sınırsız.
- **Kabul kriteri:** `tests/viewer/test_policy_runner.py` yeşil (checkpoint yükleniyor, `N_max`'tan büyük N için aksiyon üretiyor).
- **Açık sorular:** Checkpoint nasıl seçilir? Baseline ile politika arasında geçiş olsun mu?
- **Durum:** —
- **Kontrol eden:** —

---

## Onay

**Onay:** ⬜ bekliyor

## Kapanış

- [ ] Tüm paketler kabul kriterini karşıladı, farklı ajan kontrol etti
- [ ] `temp/5-*` boşaltıldı
- [ ] CHANGELOG'da sürüm kesildi, tag atıldı
- [ ] TODO durumu `✅`
