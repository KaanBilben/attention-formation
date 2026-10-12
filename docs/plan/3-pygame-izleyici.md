# Objektif 3 — Pygame izleyici

| Alan | Değer |
|---|---|
| Objektif | `viewer/`: simülasyonu izleme ve etkileşim |
| Çıktı | Çizim, pan/zoom, Space/R, Ekle/Sil Modu, baseline politika |
| Bağımlılık | Obj 1-P1 (durum sözleşmesi) |
| Açılış | 12.10.2026 |
| Durum | — |

Açık sorular paketi alan geliştiriciye şıklı sorulur (PROJECT.md §6, §11). UI görünümü test edilmez (§7); mantık (koordinat dönüşümü, tıklama → Agent eşlemesi) test edilir.

---

## İş paketleri

P1 bitince P2 başlar. P3, P1 ile paralel.

### P1 — Çizim ve kamera
- **Bağımlılık:** Obj 1-P1
- **Dosyalar:** `viewer/app.py`, `viewer/camera.py`, `tests/viewer/test_camera.py`
- **Yapılacak:** Çember, gövdeler, d_min halkaları, başarı durumu; pan/zoom; Space duraklat, R sıfırla.
- **Kabul kriteri:** `tests/viewer/test_camera.py` yeşil (dünya ↔ ekran dönüşümü); izleyici açılıyor, geliştirici gözle onaylıyor.
- **Açık sorular:** Pencere boyutu? Zoom sınırları? Neler çizilir, renkler?
- **Durum:** —
- **Kontrol eden:** —

### P2 — Ekle/Sil Modu
- **Bağımlılık:** P1, Obj 1-P4
- **Dosyalar:** `viewer/edit_mode.py`, `tests/viewer/test_edit_mode.py`
- **Yapılacak:** Mod açıkken sol tık Agent ekler, imleç Agent üzerindeyken sağ tık siler; kapalıyken sol tık pan.
- **Kabul kriteri:** `tests/viewer/test_edit_mode.py` yeşil (tıklama → ekle/sil/pan kararı, isabet testi).
- **Açık sorular:** Mod nasıl açılıp kapanır (tuş/buton)? Mod göstergesi nerede?
- **Durum:** —
- **Kontrol eden:** —

### P3 — Baseline politika
- **Bağımlılık:** Obj 1-P1
- **Dosyalar:** `viewer/baseline.py`, `tests/viewer/test_baseline.py`
- **Yapılacak:** Elle yazılmış politika: çembere yönel, komşulardan uzaklaş. Fizik/ödül hatalarını RL'den önce yakalamak ve raporda karşılaştırma tabanı.
- **Kabul kriteri:** `tests/viewer/test_baseline.py` yeşil.
- **Açık sorular:** Kural tam olarak ne? Hangi davranış test edilir?
- **Durum:** —
- **Kontrol eden:** —

---

## Onay

**Onay:** ⬜ bekliyor

## Kapanış

- [ ] Tüm paketler kabul kriterini karşıladı, farklı ajan kontrol etti
- [ ] `temp/3-*` boşaltıldı
- [ ] CHANGELOG'da sürüm kesildi, tag atıldı
- [ ] TODO durumu `✅`
