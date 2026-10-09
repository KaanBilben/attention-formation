# attention-formation

Değişken sayıda RL ajanının (tank), attention kullanarak sabit bir çembere merkezi bir atama olmadan, kendi kararlarıyla yerleşmesi ve tank sayısı değiştiğinde yeniden dağılması.

## Dil

**Tank**:
Ortamdaki tek bir öğrenen ajan; iki eksende ivme uygulayarak hareket eder ve çember üzerindeki yerini kendisi seçer.
_Kaçın_: Birim, robot, oyuncu

**Çember**:
Merkezi ve yarıçapı sabit ve bilinen hedef daire. Tankların çember üzerindeki açısı önceden belirlenmez.
_Kaçın_: Halka, yörünge

**Daire Formasyonu** (Circle Formation):
Tüm tankların çemberin üzerinde bulunduğu düzen. Eşit aralık (N=4 kare, N=6 altıgen) tercih edilir ama zorunlu değildir.
_Kaçın_: Dizilim, şekil

**Yeniden Dağılım** (Reformation):
Kullanıcı tank ekleyip çıkardığında tankların yeni duruma göre çember üzerinde yeniden yer bulması.
_Kaçın_: Yeniden dizilme, reset

**Gövde**:
Tankın sabit boyutlu fiziksel bedeni. İki gövde üst üste geçemez; birbirine dayanan tank, diğeri çekilene kadar duvara çarpmış gibi takılı kalır (sekmez).
_Kaçın_: Hitbox, çarpışma kutusu

**Çarpışma**:
İki tankın birbirine izin verilen en küçük mesafeden (d_min) daha fazla yaklaşması; fiziksel engel değil, cezalandırılan bir durumdur. d_min tank sayısı arttıkça küçülür. Daire Formasyonu çarpışmasız olmalıdır.
_Kaçın_: Üst üste binme, temas

## Eğitim

**Faz 1 (Kuruluş)**:
Tank sayısının episode boyunca sabit kaldığı, Daire Formasyonu kurulunca biten eğitim aşaması.
_Kaçın_: Ön eğitim, warm-up

**Faz 2 (Yeniden Dağılım)**:
Episode sırasında tankların rastgele eklenip çıkarıldığı ve Yeniden Dağılımın öğrenildiği eğitim aşaması.
_Kaçın_: İnce ayar, fine-tune

## Demo

**Ekle/Sil Modu** (Add/Remove Mode):
Arayüzde açılıp kapanan mod. Açıkken sol tık tıklanan noktaya tank ekler, imleç bir tankın üzerindeyken sağ tık o tankı siler. Kapalıyken sol tık ekranı kaydırır (pan).
_Kaçın_: Edit modu, düzenleme modu
