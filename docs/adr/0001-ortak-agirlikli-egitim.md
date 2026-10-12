# Tüm Agent'lar tek bir ortak ağı eğitir

Agent'lar merkezi bir atayıcı olmadan, her biri kendi gözlemiyle karar verir. Ama hepsi aynı ağın güncel halini kullanır ve her Agent'ın bireysel ödülüyle ürettiği deneyim, bu tek ağı günceller (parameter sharing). Görev işbirlikçi olduğu için, rekabetçi self-play'den gelen "tek öğrenen + eski modellerin donmuş kopyaları" yöntemini seçmedik.

## Değerlendirilen seçenekler

- **Tek öğrenen + donmuş eski modeller:** SB3'e doğrudan uyuyordu. Reddedildi, çünkü öğrenen Agent eski takım arkadaşlarına uyum sağlamayı öğreniyor ve demoda bütün Agent'lar yeni modeli kullandığında dağılım kayıyor. Üstelik her adımda N Agent'ın yalnızca birinin deneyimi kullanılıyor.

## Sonuçlar

- SB3 her adımda sabit sayıda Agent beklediği için, Agent'ların eklenip çıkarıldığı bu düzene uymuyor. Agent'ların gelip gitmesini doğal olarak desteklediği için RLlib (MultiAgentEnv; tüm Agent'lar tek bir policy'ye bağlanır) seçildi.
