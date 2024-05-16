# El Hareketleriyle Acil Durum Bildirme Uygulaması

Bu uygulama, kullanıcıların belirli el hareketlerini kullanarak acil durum mesajlarını otomatik olarak gönderebilecekleri bir arayüz sağlar. Kullanıcılar, program aracılığıyla bir telefon numarası ve acil durum mesajını tanımlar. Ardından, belirli bir el hareketi gerçekleştirildiğinde program, tanımlı telefon numarasına belirtilen mesajı anında gönderir.

## Başlarken

Bu talimatlar, projenin yerel bir makinede nasıl çalıştırılacağını size adım adım gösterecektir.

### Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python kütüphanelerini yüklemeniz gerekmektedir:

- `tkinter`
- `cv2` (OpenCV)
- `mediapipe`
- `pywhatkit`

Yukarıdaki kütüphaneleri yüklemek için aşağıdaki komutu kullanabilirsiniz:

(`pip install tkinter opencv-python mediapipe pywhatkit`)

(`pip install -r requirements.txt`)
Bu komut, requirements.txt dosyasındaki her bir satırdaki paketleri yükleyecektir. Bu şekilde, projenin gereksinimlerini tek bir adımda yükleyebilirsiniz.


### Kurulum

1. Bu projeyi klonlayın:
git clone https://github.com/kullanici/El-Hareketleriyle-Acil-Durum-Bildirme-Uygulamasi.git

2. Proje dizinine gidin:
cd El-Hareketleriyle-Acil-Durum-Bildirme-Uygulamasi

3. Ana Python dosyasını çalıştırın:
python (`HandTrackin.py`)

## Kullanım

1. Telefon numarasını ve acil durum mesajını girin.
2. "Programı Başlat" düğmesine tıklayın.
3. Videoda belirtilen el hareketlerini yapın:
   - İlk hareket: Belirtilen el hareketlerini gerçekleştirin.
   - İkinci hareket: Belirli el hareketlerini bir kez daha gerçekleştirin.
   - Üçüncü hareket: İlk iki hareketi ve belirli bir başparmak hareketini gerçekleştirin.
4. Mesaj, belirtilen telefon numarasına gönderilecektir.

## Katkıda Bulunma

Bu proje geliştirilmeye açıktır. Katkıda bulunmak için:

1. Fork yapın (https://github.com/kullanici/El-Hareketleriyle-Acil-Durum-Bildirme-Uygulamasi/fork)
2. Yeni bir özellik dalı oluşturun (`git checkout -b ozellik/yeni-ozellik`)
3. Değişikliklerinizi commit edin (`git commit -am 'Yeni özellik: Yeni özellik açıklaması'`)
4. Dalınıza itin (`git push origin ozellik/yeni-ozellik`)
5. Bir Birleştirme İsteği (Pull Request) gönderin
