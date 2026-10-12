# attention-formation

Değişken sayıda Agent'ın attention kullanarak, merkezi atama olmadan sabit bir çembere yerleşmesi ve Agent sayısı değiştiğinde yeniden dağılması.

## Durum

Kurulum tamamlandı. Sıradaki objektif: [TODO.md](TODO.md)

## Yapı

```
PROJECT.md      çalışma kuralları, komutlar, mimari: tek kaynak
GLOSSARY.md     kavramlar
TODO.md         objektifler
CHANGELOG.md    değişiklikler (Keep a Changelog)
docs/adr/       mimari kararlar
docs/plan/      objektif planları ve iş paketleri
temp/           geçici denemeler; objektif kapanışında boşaltılır
src/attention_formation/   kod
tests/          testler
```

## Kurulum (CPU)

```sh
python -m venv .venv
.venv/Scripts/python -m pip install torch --index-url https://download.pytorch.org/whl/cpu
.venv/Scripts/python -m pip install -e ".[dev]"
.venv/Scripts/python -m pytest
```

Diğer komutlar ve GPU'ya geçiş: [PROJECT.md](PROJECT.md) §1.

## Nasıl çalışıyoruz

Objektif paketlere bölünür → **onay alınır** → paket havuzdan alınır → test önce uygulanır → farklı bir ajan PR'ı kabul kriterine karşı kontrol eder → kaydedilir.

Ayrıntı: [PROJECT.md](PROJECT.md)
