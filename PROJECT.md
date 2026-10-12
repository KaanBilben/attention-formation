# attention-formation — Çalışma Düzeni

| Alan | Değer |
|---|---|
| Amaç | Değişken sayıda Agent'ın attention kullanarak, merkezi atama olmadan sabit bir çembere yerleşmesi ve Agent sayısı değiştiğinde yeniden dağılması |
| Çalışma dili | Türkçe |
| Kurulum | 12.10.2026 |

Bu dosya projenin **tek kural kaynağıdır**. `CLAUDE.md` ve `AGENTS.md` yalnızca buraya yönlendirir ve rol bildirir; kural kopyalanmaz. Kural değişecekse burada değişir.

---

## 0. Çalışma dili

Proje Türkçe yürütülür: yanıtlar, dokümanlar, TODO maddeleri, commit mesajları, kod içi yorumlar.

Kod kimlikleri (değişken, fonksiyon, sınıf, dosya adı) ve **test adları** İngilizce kalır.

**Üslup:** Kısa ve öz. Anlam kaybı olmadan mümkün olan en kısa hal. Tekrar, süsleme ve gereksiz tablo yok.

---

## 1. Proje

Değişken sayıda RL Agent'ı, sabit merkez ve yarıçaplı bir çember üzerinde Daire Formasyonu kurar. Agent'lar kimin nereye geçeceğini merkezi bir atayıcıdan almaz; her biri kendi gözlemiyle karar verir. Kullanıcı Agent ekleyip çıkardığında kalanlar yeniden dağılır.

- Kavramlar: [GLOSSARY.md](GLOSSARY.md). Kodda ve konuşmada oradaki terimler kullanılır.
- Mimari kararlar: [docs/adr/](docs/adr/)

### Teknoloji

Python ≥3.11 (geliştirme 3.13), RLlib (PPO, `MultiAgentEnv`, özel RLModule), PyTorch (şimdilik CPU), numpy, Pygame. Test: pytest. Lint/format: ruff.

### Komutlar

```sh
# Kurulum (CPU)
python -m venv .venv
.venv/Scripts/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv/Scripts/python -m pip install -e ".[dev]"

# Test
.venv/Scripts/python -m pytest                                    # hepsi
.venv/Scripts/python -m pytest tests/sim/test_dynamics.py          # tek dosya
.venv/Scripts/python -m pytest tests/sim/test_dynamics.py::test_x  # tek test

# Lint / format
.venv/Scripts/python -m ruff check .
.venv/Scripts/python -m ruff format .
```

GPU'ya geçiş: torch CUDA index'inden kurulur, [config.py](src/attention_formation/config.py) içinde `device="cuda"`, `num_gpus=1`. Cihaz seçimi başka yerde yapılmaz.

### Kod alanları

Hepsi `src/attention_formation/` altında:

| Alan | Ne tutar | Bağımlılık yönü |
|---|---|---|
| `config.py` | Tüm sabitler (R, gövde, a_max, v_max, sürtünme, d₀, α, ε, T, N_max, cihaz) | — |
| `sim/` | Fizik, gövde örtüşmezliği, Agent ekle/çıkar, ödül, başarı, gözlem. **RL ve Pygame'den bağımsız**, saf numpy | config |
| `env/` | `sim/`'i RLlib `MultiAgentEnv` olarak sarar (doğma, sonlanma, Faz 1/2) | sim |
| `models/` | Attention RLModule: maskeli attention, actor + critic (IPPO) | gözlem sözleşmesi |
| `training/` | PPO eğitimi, müfredat, checkpoint | env, models |
| `viewer/` | Pygame izleyici, Ekle/Sil Modu, baseline politika, checkpoint oynatma | sim (+ models) |

`sim/` çekirdektir; `env/` ve `viewer/` ona bağlanır, ama `sim/` hiçbirine bağlanmaz. Eğitimde gözlem `N_max`'a kadar padding + maske ile sabit boyuttadır. İzleyici modeli doğrudan çağırdığı için N sınırsızdır.

Klasörler önceden açılmaz, ihtiyaç anında açılır. Bir dosyanın nereye gideceği belirsizse §11.

---

## 2. Kapsam — yaşayan liste

### Kapsam dışı

- **Düşman, vurulma, çatışma mekaniği.** Agent sayısı yalnızca kullanıcı veya eğitim olayıyla değişir.
- **Çoklu halka formasyonu.** Çembere sığmayan Agent'lar dışarıda kalır; başarısızlık gözlemlenir.
- **Gerçekçi araç kinematiği** (diferansiyel sürüş vb.). İki eksende ivme yeterli; Agent herhangi bir aracı temsil eder.
- **Merkezi atama ile çözüm** (ör. Hungarian). Agent'lar yerini kendisi seçer; projenin konusu budur.
- **Agent başına ayrı ağırlıklar.** [ADR 0001](docs/adr/0001-ortak-agirlikli-egitim.md).
- **Web arayüzü.** Demo yalnızca Pygame.

**Kural:** Bu listedeki iş yapılmaz. Bir işin listede olup olmadığı belirsizse durulur ve sorulur (§11).

**Bu liste eksiktir.** Karşılaşıldıkça büyür: bir sınır sorusu cevaplandığında buraya yazılır ve CHANGELOG'a satır düşülür.

---

## 3. Değişmezler — yaşayan liste

Pazarlık dışı. Her işte geçerli, gerekçe istemez, "bu sefer istisna" olmaz.

- **D-1** Gövdeler hiçbir adımda örtüşmez.
- **D-2** Hız ve ivme sınırları hiçbir adımda aşılmaz.
- **D-3** Politika, diğer Agent'ların sırasından bağımsızdır (permütasyon değişmezliği).
- **D-4** Padding çıktıyı değiştirmez; politika eğitimdeki `N_max`'tan büyük N ile de çalışır.
- **D-5** Aynı seed ile simülasyon aynı trajektoriyi üretir.

Her değişmez `D-<no>` numarası taşır ve numarasıyla bir teste bağlanır (§7). **Numarasız veya testsiz değişmez olmaz.** Yeni değişmez eklendiğinde testi de eklenir.

Yeni değişmezi yalnızca geliştiriciler (insanlar) ekler; ajan önerir, ekleyemez.

---

## 4. Ekip ve sahiplik

| Kim | Rol |
|---|---|
| İki geliştirici (insan) | Karar ve onay. Havuzdan paket alır, kendi ajanlarıyla yürütür. |
| Claude (ikisi de) | Beyin/planlayıcı ve ana geliştirici: objektifi paketlere böler, paket uygular, entegre eder. |
| Codex / OpenCode | Basit paketlerde geliştirici. |

**Sahiplik yok, havuz var.** Objektiflerin sahibi yoktur. Bağımlılığı bitmiş paketi, geliştiricilerden biri alır:

1. `git pull`
2. Plan dosyasında paketin **Durum** alanını `▶ @<git kullanıcı adı>` yapar
3. Bu tek değişikliği hemen `main`'e push eder. Push çakışırsa paketi diğeri almıştır; pull edip başka paket seçilir.

Kurallar:

- **Depo tek iletişim kanalıdır.** Karar, durum ve not depoya yazılır.
- Başkasının aldığı pakette kod yazılmaz; görülen sorun plan dosyasına not olarak bırakılır.
- Aynı dosyada eşzamanlı çalışma yok. Paketler bu yüzden dosya bazında çakışmasız bölünür.

---

## 5. Dosya düzeni

Düzenin amacı: **neyin nerede olduğunun her an bilinmesi.**

### Kök — beyaz liste

Kökte yalnızca şu markdown dosyaları bulunur:

```
PROJECT.md  CLAUDE.md  AGENTS.md  TODO.md  CHANGELOG.md  README.md  GLOSSARY.md
```

Başka hiçbir markdown kökte olmaz. Hook bunu zorlar.

### `docs/`

Beyaz liste dışındaki **tüm** markdown dosyaları burada.

```
docs/
├── adr/
│   └── <nnnn>-<konu>.md      mimari karar kaydı
├── plan/
│   └── <obj-no>-<konu>.md    objektif planı ve iş paketleri — §6
└── <konu>.md                 diğer dokümanlar
```

### `temp/`

Geçici ve deneysel her şey. Her deneme **kendi alt klasöründe**:

```
temp/
└── <obj-no>-<konu>/
    ├── NOT.md      neden var · ne deneniyor · ne zaman gidecek
    └── ...
```

`temp/` git'e girer; deneme diğer geliştiriciye de görünmelidir.

**Ömür kuralı:** Objektif kapanmadan `temp/` boşaltılır. İçerik ya ilgili klasöre taşınır ya silinir. **Dolu `temp/` ile objektif kapanmaz.**

---

## 6. Yürütme akışı

```
1  Objektif seç      TODO.md'den
2  Netleştir         belirsiz veya çakışan kavram varsa SOR — varsayma (§11)
3  Paketlere böl     paralel çalışılabilir, dosya bazında çakışmasız,
                     her pakette bağımlılık ve kabul kriteri
4  ONAY              onay yoksa iş başlamaz
5  Paket al          havuzdan, §4
6  Netleştir         paketin "nasıl"ı plan dosyasında yazmaz; paketi alan
                     geliştiriciye şıklı sorularla sorulur (§11)
7  Uygula            test önce (§7)
8  Kontrol           farklı ajan, PR üzerinde (§7, §9)
9  Kaydet            CHANGELOG + plan dosyasında paket durumu + TODO
```

### Onay kapısı

Objektif paketlere bölündüğünde, tek satır kod yazılmadan önce sunulur:

```
NE           tek cümle
NEREDE       dokunulacak dosyalar
NASIL        2-4 madde
YOL AYRIMI   (varsa) A / B · öneri · gerekçe · gelecekteki hedefe etkisi
RİSK         (varsa)
```

Onayı geliştiricilerden biri verir ve plan dosyasına yazılır. İstisna: basit fix ve planda kapsamı netleşmiş paket.

**Yol ayrımı kuralı:** İki yoldan biri seçilecekse seçim yalnızca bugünkü işe göre değil, **ilerideki objektiflere göre** yapılır.

### Plan dosyası

Objektif açılınca `docs/plan/<no>-<konu>.md` yazılır: objektif, iş paketleri (bağımlılık, dosyalar, kabul kriteri, durum, kontrol eden), onay kaydı. Objektif kapanınca dosya silinmez.

**TODO.md yalnızca objektifleri tutar**, iş paketlerini tutmaz.

---

## 7. Kontrol

### a) Kabul kriteri — her pakette zorunlu

Paket tanımlanırken "bitti" ne demek **ölçülebilir** yazılır ve mümkünse bir test dosyasına işaret eder: "`tests/sim/test_bodies.py` yeşil". Kabul kriteri olmayan paket dağıtılmaz.

### b) Çapraz kontrol — varsayılan

**Paketi yazan ajan kendi işini onaylamaz.** Kontrolü farklı bir ajan yapar (Codex'in yazdığını Claude, Claude'un yazdığını Codex/OpenCode ya da diğer geliştiricinin Claude'u). Kontrol PR üzerinde, kabul kriterine karşı yapılır ve plan dosyasındaki **Kontrol eden** alanına yazılır.

### c) Üçüncü göz — talep üzerine

Geri alınamaz kararlar (ADR'ler, gözlem/aksiyon sözleşmesi, ödül yapısı) için diğer geliştirici devreye girer.

**Bulgu yazarken** hangi kriterin veya kuralın ihlal edildiği belirtilir. "İyi görünmüyor" yeterli değil.

---

### Test disiplini: test önce

Testler **koda göre değil, beklenen davranışa göre** yazılır. Bu yüzden önce yazılır:

1. Davranışın testi yazılır
2. Çalıştırılır, **kırmızı görülür**. Doğrudan yeşil gören test o davranışa bağlı değildir.
3. Kod yazılır, test yeşile döner

Test, paketin kabul kriterinin çalıştırılabilir halidir: kriterin gerektirdiğinden geniş yazılmaz.

**Nerede yapılmaz:** `temp/` altında (deneme, test oraya taşınırken yazılır), UI görünümü, trivial erişimciler.

**Kapsam yüzdesi hedefi yoktur.**

**Bug fix'te:** Refleksle test eklenmez. Önce sorulur: *mevcut testlerden hangisi bunu yakalamalıydı?* Zayıf test varsa güçlendirilir; yoksa bir test eklenir.

### Test yapısı

| Tür | Ne doğrular |
|---|---|
| **Birim** | Tek davranış. Bir test = bir kural. |
| **Sözleşme** | Paketler arası sınır: durum sözleşmesi (`sim/`), gözlem sözleşmesi (`sim/` ↔ `models/`), env ↔ RLlib. |
| **Değişmez** | §3'e birebir bağlı. **Asla silinmez, zayıflatılmaz.** |

```
tests/
├── <alan>/       kod alanlarını aynalar: tests/sim/, tests/env/, tests/models/ ...
└── degismez/     §3'e bağlı: tests/degismez/test_d1_<davranis>.py
```

**Adlandırma:** Test adı davranışı İngilizce bir cümle olarak yazar: `test_bodies_never_overlap_after_step` ✓, `test_physics_2` ✗. Assert mesajı beklenen ve bulunan değeri içerir.

**Bakım:** Objektif kapanışında aynı şeyi doğrulayan testler birleştirilir.

---

## 8. Kayıt

### CHANGELOG.md

[Keep a Changelog 1.1.0](https://keepachangelog.com/tr-TR/1.1.0/) standardı, [SemVer](https://semver.org/lang/tr/).

- İşler `## [Unreleased]` altında `Added` / `Changed` / `Deprecated` / `Removed` / `Fixed` / `Security` başlıklarına yazılır.
- Satır, değişikliği kullanıcı/geliştirici gözünden anlatır; objektif numarası sonda: `- Gövde örtüşmezliği (obj-1)`.
- **Bir objektif kapanınca sürüm kesilir:** `[Unreleased]` → `## [0.<n>.0] - YYYY-MM-DD`, `pyproject.toml` versiyonu güncellenir, `v0.<n>.0` git tag'i atılır, dosya sonundaki karşılaştırma linkleri güncellenir.

### TODO.md

| Durum | Anlam |
|---|---|
| `—` | başlamadı |
| `▶` | devam ediyor |
| `✅ <tarih>` | bitti |
| `[bekliyor: <ne>]` | karar bekliyor, başlamaz |

**CHANGELOG ve plan dosyasındaki paket durumu güncellenmeden iş tamamlanmış sayılmaz.**

---

## 9. Git

- **Paket başına branch:** `obj-<no>-p<paket>` (ör. `obj-1-p3`), kısa ömürlü.
- **PR ile main'e:** farklı bir ajan kabul kriterine karşı kontrol eder (§7b), sonra merge.
- **İstisna:** paket sahiplenme (§4) ve yalnız doküman/durum güncellemesi doğrudan `main`'e.
- **Commit:** `[obj-no] açıklama (@ajan)` → `[1] Gövde örtüşmezliği (@claude)`. Objektife bağlı değilse `[genel]`.
- İşe başlamadan `git pull`. `main`'e kırık test gönderilmez.

---

## 10. Dokümantasyon eşiği

Şu üçünden **biri** varsa `docs/` altına doküman (gerekirse ADR) yazılır:

- birden fazla alana dokunuyor
- yeni bağımlılık veya teknoloji getiriyor
- geri alınması pahalı: gözlem/aksiyon sözleşmesi, ödül yapısı, checkpoint formatı

Hiçbiri yoksa doğrudan yapılır.

---

## 11. Belirsizlikte dur, şıklı sor

**Hiçbir şey tahmin edilmez, hiçbir çıkarım kendiliğinden yapılmaz.** Şu durumlarda iş durur ve sorulur:

- Bir kavram [GLOSSARY.md](GLOSSARY.md) ile çakışıyor veya belirsiz
- İşin kapsam içinde olup olmadığı belirsiz
- Bir dosyanın nereye gideceği belirsiz
- Bir paketin nasıl yapılacağı plan dosyasında yazmıyor
- İki yoldan hangisinin seçileceği ilerideki objektifleri etkiliyor

**Soru biçimi:** Şıklı sorulur ve şıklardan biri önerilen cevaptır (ilk şık, "(Önerilen)"). Serbest cevap için yer bırakılır. Ortamdan bulunabilecek bir bilgi (dosya, sürüm, komut çıktısı) sorulmaz, bakılır.

Verilen cevap ilgili yere yazılır (§2, §3, GLOSSARY, plan dosyası veya ADR) ve CHANGELOG'a gerekiyorsa satır düşülür. Aynı soru ikinci kez sorulmaz.
