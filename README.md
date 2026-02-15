
# 🚗 Webots Otonom Araç Navigasyon Simülasyonu

Bu projede Webots simülasyon ortamında GPS, pusula (Compass), IMU ve Lidar sensörleri kullanılarak waypoint tabanlı otonom araç navigasyonu gerçekleştirilmiştir. Araç, belirlenen hedef noktalara (waypoint) yönelerek konum ve yön hatasını minimize edecek şekilde hareket etmektedir.

---

## 🎯 Proje Amacı

Simülasyon ortamında bir aracın:

- GPS ile konumunu belirlemesi,
- Pusula verisi ile yönünü hesaplaması,
- IMU ile yönelim bilgisini doğrulaması,
- Waypoint tabanlı hedef takibi yapması,
- Basit kontrol algoritması ile direksiyon açısını ayarlaması

amaçlanmıştır.

---

## 🧠 Kullanılan Sensörler

- 📍 **GPS** → Anlık X-Y konum bilgisi
- 🧭 **Compass (Pusula)** → Yaw (baş yönü) hesaplama
- 📐 **IMU** → Araç yönelim verisi
- 📡 **Lidar** → Çevre algılama (varsa)

---

## ⚙️ Kontrol Algoritması

Hedef noktaya yönelmek için önce hedef açısı hesaplanır:

θ_target = atan2(dy, dx)
Aracın mevcut yönü (yaw):

θ_yaw
Yön hatası:

θ_error = θ_target - θ_yaw
Direksiyon açısı basit oransal kontrol ile belirlenmiştir:

steering_angle = Kp × θ_error


Direksiyon açısı belirli sınırlar içerisinde tutulmuştur.

---

## 🗂 Proje Yapısı



controllers/ → Python kontrol kodu
protos/ → Araç model dosyaları
worlds/ → Simülasyon ortamı (.wbt)


---

## ▶️ Çalıştırma Adımları

1. Webots programını açın  
2. `worlds` klasöründeki `.wbt` dosyasını yükleyin  
3. Simülasyonu başlatın  
4. Araç belirlenen waypoint'leri takip edecektir  

---

## 🛠 Kullanılan Teknolojiler

- Webots
- Python
- GPS Sensörü
- Compass Sensörü
- IMU
- Lidar

---

## 👨‍💻 Not

Bu proje staj çalışması kapsamında geliştirilmiş bir otonom araç navigasyon sistemidir.



# 🚗 Webots Autonomous Vehicle Navigation Simulation

This project implements waypoint-based autonomous vehicle navigation in the Webots simulation environment using GPS, Compass, IMU, and Lidar sensors. The vehicle moves toward predefined waypoints while minimizing position and heading error.

---

## 🎯 Project Objective

The objective of this project is to enable a simulated vehicle to:

- Determine its position using GPS
- Estimate its heading using Compass data
- Verify orientation using IMU data
- Track predefined waypoints
- Adjust steering angle using a basic control algorithm

---

## 🧠 Sensors Used

- 📍 **GPS** → Real-time X-Y position data
- 🧭 **Compass** → Yaw (heading) estimation
- 📐 **IMU** → Orientation data
- 📡 **Lidar** → Environment perception (if available)

---

## ⚙️ Control Algorithm

To move toward the target waypoint, the target heading angle is calculated as:

θ_target = atan2(dy, dx)

Current vehicle heading (yaw):

θ_yaw

Heading error:

θ_error = θ_target - θ_yaw

The steering angle is computed using proportional control:

steering_angle = Kp × θ_error

The steering angle is limited within predefined bounds.

---

## 🗂 Project Structure

controllers/ → Python control code  
protos/ → Vehicle model files  
worlds/ → Simulation environment (.wbt)

---

## ▶️ How to Run

1. Open Webots  
2. Load the `.wbt` file from the `worlds` directory  
3. Start the simulation  
4. The vehicle will follow predefined waypoints  

---

## 🛠 Technologies Used

- Webots
- Python
- GPS Sensor
- Compass Sensor
- IMU
- Lidar

---

## 👨‍💻 Note

This project was developed as part of an internship study focusing on autonomous vehicle navigation in simulation.







