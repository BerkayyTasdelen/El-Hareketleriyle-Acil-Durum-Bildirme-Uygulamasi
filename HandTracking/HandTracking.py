import tkinter as tk
from tkinter import messagebox, scrolledtext
import cv2
import mediapipe as mp
import pywhatkit as kit
import threading

tel_no = ""  # Telefon numarası
mesaj1 = ""  # Mesaj metni
is_message_sent = False  # Mesajın gönderilip gönderilmediğini kontrol etmek için bayrak


def set_phone_number():  # Telefon numarası girişini ayarlayan fonksiyon
    global tel_no
    tel_no = tel_entry.get()  # Giriş alanından telefon numarasını al
    messagebox.showinfo("Bilgi", f"Telefon numarası başarıyla kaydedildi: {tel_no}")  # Bilgi mesajı


def set_message():  # Mesajı ayarlayan fonksiyon
    global mesaj1
    mesaj1 = message_text.get("1.0", tk.END)  # Metin alanından mesajı al
    messagebox.showinfo("Bilgi", "Acil durum mesajı başarıyla kaydedildi.")  # Bilgi mesajı


def send_message():  # Mesajı gönderen fonksiyon
    global is_message_sent
    if not is_message_sent:
        kit.sendwhatmsg_instantly(tel_no, mesaj1)  # PyWhatKit kullanarak mesajı gönder
        is_message_sent = True


def start_program():  # Programı başlatan fonksiyon
    global tel_no, mesaj1
    if tel_no == "":
        messagebox.showerror("Hata", "Lütfen önce telefon numarasını girin.")  # Hata mesajı: Telefon numarası girilmedi
        return

    if mesaj1 == "":
        messagebox.showerror("Hata", "Lütfen önce acil durum mesajını girin.")  # Hata mesajı: Mesaj girilmedi
        return

    cap = cv2.VideoCapture("elizleme2.MOV")  # Video yakalama cihazı oluştur
    mpHands = mp.solutions.hands  # Mediapipe ile elleri algılamak için
    hands = mpHands.Hands()  # Elleri algılamak için Hands sınıfı
    mpDraw = mp.solutions.drawing_utils  # Elleri çizmek için yardımcı fonksiyonlar

    control1 = False  # Kontrol bayrağı
    control2 = False  # Kontrol bayrağı

    img_stage0 = cv2.imread("yardim0.jpg")  # Yardım resimlerini yükle
    img_stage1 = cv2.imread("yardim1.jpg")  # Yardım resimlerini yükle
    img_stage2 = cv2.imread("yardim2.jpg")  # Yardım resimlerini yükle
    img_stage3 = cv2.imread("yardim3.jpg")  # Yardım resimlerini yükle

    fingerCoordinates = [(8, 6), (12, 10), (16, 14), (20, 18)]  # Parmak koordinatları
    thumbCoordinates = [(4, 2)]  # Başparmak koordinatları

    while True:  # Sonsuz döngü
        success, img = cap.read()  # Kameradan bir kare oku
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR'yi RGB'ye dönüştür
        results = hands.process(imgRGB)  # Elleri işle
        multiLandmarks = results.multi_hand_landmarks  # Birden çok eli al

        if multiLandmarks:
            handPoints = []  # Ellerin koordinatları
            for handLms in multiLandmarks:
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)  # Ellerin bağlantılarını çiz
                for idx, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    handPoints.append((cx, cy))  # Ellerin koordinatlarını listeye ekle

            for point in handPoints:
                cv2.circle(img, (point[0], point[1]), 5, (0, 0, 10), cv2.FILLED)  # Ellerin etrafına daire çiz
                cv2.circle(img, (point[0], point[1]), 3, (225, 225, 225), cv2.FILLED)  # Ellerin etrafına daire çiz

            img[0:img_stage0.shape[0], 0:img_stage0.shape[1]] = img_stage0  # Yardım resmini ekrana koy

            for coordinate in fingerCoordinates:
                if (handPoints[8][1] < handPoints[6][1]
                        and handPoints[12][1] < handPoints[10][1]
                        and handPoints[16][1] < handPoints[14][1]
                        and handPoints[20][1] < handPoints[18][1]
                        and handPoints[4][0] < handPoints[2][0]):
                    cv2.putText(img, str("stage >> 1"), (825, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2,
                                cv2.LINE_AA)  # Aşama etiketi ekle
                    for point in handPoints:
                        cv2.circle(img, (point[0], point[1]), 3, (0, 0, 255), cv2.FILLED)  # Parmak uçlarına daire çiz
                        img[0:img_stage1.shape[0], 0:img_stage1.shape[1]] = img_stage1  # Yardım resmini ekrana koy
                        control1 = True  # Kontrol bayrağını ayarla

            for coordinate in fingerCoordinates:
                if (handPoints[8][1] < handPoints[6][1]
                        and handPoints[12][1] < handPoints[10][1]
                        and handPoints[16][1] < handPoints[14][1]
                        and handPoints[20][1] < handPoints[18][1]
                        and handPoints[4][0] > handPoints[2][0]
                        and control1 == True):
                    cv2.putText(img, str("stage >> 2"), (825, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 235), 2,
                                cv2.LINE_AA)  # Aşama etiketi ekle
                    for point in handPoints:
                        cv2.circle(img, (point[0], point[1]), 3, (0, 255, 235), cv2.FILLED)  # Parmak uçlarına daire çiz
                        img[0:img_stage2.shape[0], 0:img_stage2.shape[1]] = img_stage2  # Yardım resmini ekrana koy
                        control2 = True  # Kontrol bayrağını ayarla

            for coordinate in fingerCoordinates:
                if (handPoints[8][1] > handPoints[6][1]
                        and handPoints[12][1] > handPoints[10][1]
                        and handPoints[16][1] > handPoints[14][1]
                        and handPoints[20][1] > handPoints[18][1]
                        and handPoints[4][0] > handPoints[2][0]
                        and control2 == True):
                    cv2.putText(img, str("stage >> 3"), (825, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 2,
                                cv2.LINE_AA)  # Aşama etiketi ekle

                    # Mesajı sadece bir kere göndermek için bayrağı kontrol et
                    send_message()

                    for point in handPoints:
                        cv2.circle(img, (point[0], point[1]), 3, (0, 255, 0), cv2.FILLED)  # Parmak uçlarına daire çiz
                        img[0:img_stage3.shape[0], 0:img_stage3.shape[1]] = img_stage3  # Yardım resmini ekrana koy

        cv2.imshow("Ellerin Kontrol", img)  # Ellerin kontrol ekranını göster
        if cv2.waitKey(1) & 0xFF == ord("q"):  # 'q' tuşuna basılırsa döngüyü kır
            break

    cap.release()  # Kamera yakalamasını serbest bırak
    cv2.destroyAllWindows()  # Pencereleri kapat


# Tkinter Arayüzü
root = tk.Tk()  # Ana pencereyi oluştur
root.title("Ellerin Kontrol Programı")  # Pencere başlığı
root.geometry("600x500")  # Pencere boyutu

# Arka plan rengini değiştir
root.configure(bg='#f0f0f0')

tel_label = tk.Label(root, text="Telefon Numarası:", font=("Helvetica", 12), bg='#f0f0f0')  # Telefon numarası etiketi
tel_label.pack()

tel_entry = tk.Entry(root, font=("Helvetica", 12))  # Telefon numarası giriş alanı
tel_entry.pack()

tel_button = tk.Button(root, text="Numarayı Kaydet", command=set_phone_number, font=("Helvetica", 12), bg='#4CAF50', fg='white')  # Kaydet butonu
tel_button.pack()

message_label = tk.Label(root, text="Acil Durum Mesajı:", font=("Helvetica", 12), bg='#f0f0f0')  # Mesaj etiketi
message_label.pack()

message_text = scrolledtext.ScrolledText(root, width=30, height=5, font=("Helvetica", 12))  # Mesaj giriş alanı
message_text.pack()

message_button = tk.Button(root, text="Mesajı Kaydet", command=set_message, font=("Helvetica", 12), bg='#4CAF50', fg='white')  # Kaydet butonu
message_button.pack()

start_button = tk.Button(root, text="Programı Başlat", command=start_program, font=("Helvetica", 12), bg='#008CBA', fg='white')  # Başlat butonu
start_button.pack()

root.mainloop()  # Ana döngüyü başlat