from controller import Robot, GPS, Compass, InertialUnit, Motor
import math

# Simülasyon adımı
ZAMAN_ADIMI = 32

# Robot oluştur
robot = Robot()

# Sensörleri al
gps = robot.getDevice("gps")
pusula = robot.getDevice("pusula")
imu = robot.getDevice("imu")

gps.enable(ZAMAN_ADIMI)
pusula.enable(ZAMAN_ADIMI)
imu.enable(ZAMAN_ADIMI)

# Motorları al
sol_on = robot.getDevice("left_front_wheel")
sag_on = robot.getDevice("right_front_wheel")
sol_direksiyon = robot.getDevice("left_steer")
sag_direksiyon = robot.getDevice("right_steer")

sol_on.setPosition(float("inf"))
sag_on.setPosition(float("inf"))

# Hedef noktalar (X, Y) → bunları sen yol segmentlerinden alıp değiştirebilirsin
waypoints = [
    (8.4, 0.5),    # Başlangıç
    (30.0, -10.0), # Orta nokta
    (60.0, -20.0)  # İleri hedef
]
hedef_index = 0

def hedefe_git():
    global hedef_index

    # Mevcut GPS pozisyonu
    pos = gps.getValues()
    x, y = pos[0], pos[1]

    # Şu anki hedef
    hedef_x, hedef_y = waypoints[hedef_index]

    # Hedefe olan açı farkı
    dx = hedef_x - x
    dy = hedef_y - y
    hedef_acisi = math.atan2(dy, dx)

    # Pusuladan yaw açısı
    pusula_veri = pusula.getValues()
    yaw = math.atan2(pusula_veri[0], pusula_veri[2])

    # Hata (dönme açısı farkı)
    aci_farki = hedef_acisi - yaw
    while aci_farki > math.pi:
        aci_farki -= 2 * math.pi
    while aci_farki < -math.pi:
        aci_farki += 2 * math.pi

    # Direksiyon kontrolü (basit oransal kontrol)
    direksiyon_acisi = 0.5 * aci_farki
    direksiyon_acisi = max(min(direksiyon_acisi, 0.5), -0.5)  # sınırlama

    # Motorlara uygula
    hiz = 5.0
    sol_on.setVelocity(hiz)
    sag_on.setVelocity(hiz)
    sol_direksiyon.setPosition(direksiyon_acisi)
    sag_direksiyon.setPosition(direksiyon_acisi)

    # Konsola yazdır
    print("----------------------------")
    print(f"GPS -> X:{x:.2f}, Y:{y:.2f}")
    print(f"Hedef -> X:{hedef_x:.2f}, Y:{hedef_y:.2f}")
    print(f"Pusula Yaw -> {yaw:.2f}")
    print(f"Direksiyon Açısı -> {direksiyon_acisi:.2f}")

    # Hedefe ulaşıldı mı?
    if math.hypot(dx, dy) < 2.0:  # 2 metre yakınsa hedef tamam
        hedef_index += 1
        if hedef_index >= len(waypoints):
            print("🚗 Tüm hedefler tamamlandı!")
            return False
    return True

# Ana döngü
while robot.step(ZAMAN_ADIMI) != -1:
    if not hedefe_git():
        break
