# Objektif 1 — Simülasyon çekirdeği

| Alan | Değer |
|---|---|
| Objektif | `sim/`: dinamik, gövde örtüşmezliği, Agent ekle/çıkar, başarı, ödül, gözlem |
| Çıktı | RL ve Pygame'den bağımsız, saf numpy, testli çekirdek |
| Bağımlılık | — |
| Açılış | 12.10.2026 |
| Durum | — |

Paketlerin "nasıl"ı burada yazmaz. **Açık sorular** paketi alan geliştiriciye şıklı sorulur (PROJECT.md §6, §11); cevaplar bu dosyaya işlenir.

Durum: `—` hazır değil/başlamadı · `▶ @<git kullanıcı>` alındı · `✅ <tarih>` bitti

---

## İş paketleri

P1 bitince P2, P3, P4, P5, P7 paralel yürür; P6, P5'i bekler.

### P1 — Durum sözleşmesi
- **Bağımlılık:** —
- **Dosyalar:** `sim/state.py`, `sim/world.py`, `tests/sim/test_state.py`
- **Yapılacak:** Agent durumunun (konum, hız, kimlik) temsili ve dünyanın `step` arayüzü; diğer paketlerin dayandığı sınır.
- **Kabul kriteri:** `tests/sim/test_state.py` yeşil (sözleşme testi).
- **Açık sorular:** Agent kimliği nasıl verilir? Durum dizi mi, Agent nesnesi mi? `step` imzası ne?
- **Durum:** —
- **Kontrol eden:** —

### P2 — Dinamik
- **Bağımlılık:** P1
- **Dosyalar:** `sim/dynamics.py`, `tests/sim/test_dynamics.py`, `tests/degismez/test_d2_*.py`, `tests/degismez/test_d5_*.py`
- **Yapılacak:** İvme uygulama, sürtünme, hız ve ivme sınırları; seed ile determinizm.
- **Kabul kriteri:** `tests/sim/test_dynamics.py`, D-2 ve D-5 testleri yeşil.
- **Açık sorular:** Entegrasyon yöntemi? Sürtünme modeli? Sınır kırpma vektör normuna göre mi, eksen bazında mı?
- **Durum:** —
- **Kontrol eden:** —

### P3 — Gövde örtüşmezliği
- **Bağımlılık:** P1
- **Dosyalar:** `sim/bodies.py`, `tests/sim/test_bodies.py`, `tests/degismez/test_d1_*.py`
- **Yapılacak:** Gövdeler üst üste geçmez; dayanan Agent sekmeden, diğeri çekilene kadar takılı kalır.
- **Kabul kriteri:** `tests/sim/test_bodies.py` ve D-1 testi yeşil.
- **Açık sorular:** Aynı anda çoklu temas nasıl çözülür? Konum düzeltme kuralı ne?
- **Durum:** —
- **Kontrol eden:** —

### P4 — Agent ekle / çıkar
- **Bağımlılık:** P1
- **Dosyalar:** `sim/population.py`, `tests/sim/test_population.py`
- **Yapılacak:** Çalışma sırasında Agent ekleme ve çıkarma, kimlik yönetimi.
- **Kabul kriteri:** `tests/sim/test_population.py` yeşil.
- **Açık sorular:** Yeni Agent'ın başlangıç hızı? Başka bir gövdenin üstüne eklenmek istenirse ne olur? Silinen kimlik tekrar kullanılır mı?
- **Durum:** —
- **Kontrol eden:** —

### P5 — d_min, Çarpışma, Daire Formasyonu
- **Bağımlılık:** P1
- **Dosyalar:** `sim/formation.py`, `tests/sim/test_formation.py`
- **Yapılacak:** `d_min(N)`, Çarpışma tespiti, Daire Formasyonu (başarı) kontrolü.
- **Kabul kriteri:** `tests/sim/test_formation.py` yeşil (elle kurulan durumlar: kusursuz altıgen → başarı, yan yana iki Agent → Çarpışma).
- **Açık sorular:** Başarı anlık mı, K adım sürmesi mi gerekir? ε değeri? `d_min` config'te mi kalır?
- **Durum:** —
- **Kontrol eden:** —

### P6 — Ödül
- **Bağımlılık:** P5
- **Dosyalar:** `sim/reward.py`, `tests/sim/test_reward.py`
- **Yapılacak:** Agent başına bireysel ödül: radyal hata, Çarpışma cezası, eşit aralık bonusu.
- **Kabul kriteri:** `tests/sim/test_reward.py` yeşil.
- **Açık sorular:** Terim ağırlıkları? Eşit aralık bonusu formülü? Shaping (ör. potansiyel tabanlı) kullanılacak mı?
- **Durum:** —
- **Kontrol eden:** —

### P7 — Gözlem
- **Bağımlılık:** P1
- **Dosyalar:** `sim/observation.py`, `tests/sim/test_observation.py`
- **Yapılacak:** Agent'ın kendisi + diğer Agent'ların göreli konum/hızı; `N_max`'a kadar padding + maske. Obj 4 bu sözleşmeye dayanır.
- **Kabul kriteri:** `tests/sim/test_observation.py` yeşil (sözleşme testi: şekil, maske, göreli koordinat).
- **Açık sorular:** Koordinatlar kartezyen mi polar mı? Normalizasyon? N gözlemde yer alır mı? Agent'ın kendi verisi neleri içerir?
- **Durum:** —
- **Kontrol eden:** —

---

## Onay

```
NE          sim/ çekirdeği, 7 paket
NEREDE      src/attention_formation/sim/, tests/sim/, tests/degismez/
NASIL       paketlerde; açık sorular paketi alana sorulur
RİSK        P1 sözleşmesi sonradan değişirse tüm paketler etkilenir
```

**Onay:** ⬜ bekliyor

## Kapanış

- [ ] Tüm paketler kabul kriterini karşıladı ve farklı ajan kontrol etti
- [ ] `temp/1-*` boşaltıldı
- [ ] Test seti gözden geçirildi
- [ ] CHANGELOG'da sürüm kesildi (0.1.0), tag atıldı
- [ ] TODO durumu `✅`
