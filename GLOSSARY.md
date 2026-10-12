# attention-formation

Değişken sayıda Agent'ın attention kullanarak, merkezi bir atama olmadan ve kendi kararlarıyla sabit bir çembere yerleşmesi ve Agent sayısı değiştiğinde yeniden dağılması.

## Dil

**Agent**:
Ortamdaki tek bir öğrenen araç; iki eksende ivme uygulayarak hareket eder ve çember üzerindeki yerini kendisi seçer. Belirli bir araç türüne (tank, drone, robot) bağlı değildir.
_Kaçın_: Tank, ajan, birim, robot, oyuncu

**Çember**:
Merkezi ve yarıçapı sabit ve bilinen hedef daire. Agent'ların çember üzerindeki açısı önceden belirlenmez.
_Kaçın_: Halka, yörünge

**Daire Formasyonu** (Circle Formation):
Tüm Agent'ların çemberin üzerinde bulunduğu düzen. Eşit aralık (N=4 kare, N=6 altıgen) tercih edilir ama zorunlu değildir.
_Kaçın_: Dizilim, şekil

**Yeniden Dağılım** (Reformation):
Kullanıcı Agent ekleyip çıkardığında Agent'ların yeni duruma göre çember üzerinde yeniden yer bulması.
_Kaçın_: Yeniden dizilme, reset

**Gövde**:
Agent'ın sabit boyutlu fiziksel bedeni. İki gövde üst üste geçemez; birbirine dayanan Agent, diğeri çekilene kadar duvara çarpmış gibi takılı kalır (sekmez).
_Kaçın_: Hitbox, çarpışma kutusu

**Çarpışma**:
İki Agent'ın birbirine izin verilen en küçük mesafeden (d_min) daha fazla yaklaşması; fiziksel engel değil, cezalandırılan bir durumdur. d_min Agent sayısı arttıkça küçülür. Daire Formasyonu çarpışmasız olmalıdır.
_Kaçın_: Üst üste binme, temas

## Eğitim

**Faz 1 (Kuruluş)**:
Agent sayısının episode boyunca sabit kaldığı, Daire Formasyonu kurulunca biten eğitim aşaması.
_Kaçın_: Ön eğitim, warm-up

**Faz 2 (Yeniden Dağılım)**:
Episode sırasında Agent'ların rastgele eklenip çıkarıldığı ve Yeniden Dağılımın öğrenildiği eğitim aşaması.
_Kaçın_: İnce ayar, fine-tune

## Demo

**Ekle/Sil Modu** (Add/Remove Mode):
Arayüzde açılıp kapanan mod. Açıkken sol tık tıklanan noktaya Agent ekler, imleç bir Agent'ın üzerindeyken sağ tık o Agent'ı siler. Kapalıyken sol tık ekranı kaydırır (pan).
_Kaçın_: Edit modu, düzenleme modu
