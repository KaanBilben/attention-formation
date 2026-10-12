# TODO — attention-formation

Objektif listesi. **Ne** yapılacak, ne çıkacak. İş paketleri ve durumları `docs/plan/<no>-<konu>.md` içinde.

| Alan | Değer |
|---|---|
| Son güncelleme | 12.10.2026 |
| Aktif | Obj 1 (onay bekliyor) |

Durumlar: `—` başlamadı · `▶` devam · `✅ <tarih>` bitti · `[bekliyor: <ne>]` karar bekliyor

---

| # | Objektif | Çıktı | Bağımlılık | Plan | Durum |
|---|---|---|---|---|---|
| 1 | Simülasyon çekirdeği | `sim/`: dinamik, gövde örtüşmezliği, ekle/çıkar, başarı, ödül, gözlem; testli, RL'den bağımsız | — | [1](docs/plan/1-simulasyon-cekirdegi.md) | — |
| 2 | RLlib ortamı (Faz 1) | `env/`: `MultiAgentEnv`, RLlib ortam kontrolünden geçiyor | 1 | [2](docs/plan/2-rllib-ortami.md) | — |
| 3 | Pygame izleyici | `viewer/`: çizim, pan/zoom, Ekle/Sil Modu, baseline politika | 1-P1 (P2 için 1-P4) | [3](docs/plan/3-pygame-izleyici.md) | — |
| 4 | Attention RLModule | `models/`: maskeli attention, actor + critic; D-3, D-4 testleri yeşil | 1-P7 | [4](docs/plan/4-attention-modulu.md) | — |
| 5 | Faz 1 eğitimi | N ≤ 8 için başarı ≥ %80 olan checkpoint, izleyicide oynatılıyor | 2, 3, 4 | [5](docs/plan/5-faz1-egitimi.md) | — |
| 6 | Faz 2 eğitimi | Agent ekle/çıkar olaylı eğitim, N_max → 16 | 5 | — | — |
| 7 | Rapor metrikleri | Danışmana sunulacak metrikler ve grafikler | 5 | — | [bekliyor: metrik kararı] |

---

Kurallar: [PROJECT.md](PROJECT.md) §6, §8
