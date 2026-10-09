# Tüm tanklar tek bir ortak ağı eğitir

Tanklar merkezi bir atayıcı olmadan, her biri kendi gözlemiyle karar verir. Ama hepsi aynı ağın güncel halini kullanır ve her tankın bireysel ödülüyle ürettiği deneyim, bu tek ağı günceller (parameter sharing). Görev işbirlikçi olduğu için, rekabetçi self-play'den gelen "tek öğrenen + eski modellerin donmuş kopyaları" yöntemini seçmedik.

## Değerlendirilen seçenekler

- **Tek öğrenen + donmuş eski modeller:** SB3'e doğrudan uyuyordu. Reddedildi, çünkü öğrenen tank eski takım arkadaşlarına uyum sağlamayı öğreniyor ve demoda bütün tanklar yeni modeli kullandığında dağılım kayıyor. Üstelik her adımda N tankın yalnızca birinin deneyimi kullanılıyor.

## Sonuçlar

- SB3 her adımda sabit sayıda ajan beklediği için, tank eklenip çıkarılan bu düzene uymuyor. Ajanların gelip gitmesini doğal olarak desteklediği için RLlib (MultiAgentEnv; tüm tanklar tek bir policy'ye bağlanır) seçildi.
