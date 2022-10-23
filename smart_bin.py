import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)

GPIO_trig1 = 2
GPIO_echo1 = 3
GPIO_trig2 = 14
GPIO_echo2 = 15
GPIO_trig3 = 23
GPIO_echo3 = 24
GPIO_right = 11
GPIO_left = 9
GPIO_center = 10
GPIO_servo = 21
GPIO_drivein1 = 5
GPIO_drivein2 = 6
GPIO_drivein3 = 19
GPIO_drivein4 = 26


GPIO.setup(GPIO_trig1, GPIO.OUT)
GPIO.setup(GPIO_echo1, GPIO.IN)
GPIO.setup(GPIO_trig2, GPIO.OUT)
GPIO.setup(GPIO_echo2, GPIO.IN)
GPIO.setup(GPIO_trig3, GPIO.OUT)
GPIO.setup(GPIO_echo3, GPIO.IN)
GPIO.setup(GPIO_right, GPIO.IN)
GPIO.setup(GPIO_left, GPIO.IN)
GPIO.setup(GPIO_center, GPIO.IN)
GPIO.setup(GPIO_servo, GPIO.OUT)
GPIO.setup(GPIO_drivein1, GPIO.OUT)
GPIO.setup(GPIO_drivein2, GPIO.OUT)
GPIO.setup(GPIO_drivein3, GPIO.OUT)
GPIO.setup(GPIO_drivein4, GPIO.OUT)

pservo = GPIO.PWM(GPIO_servo, 50)
#pservo.start(2.5)

def distance_tutup():
    GPIO.output(GPIO_trig1, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_trig1, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_echo1) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_echo1) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime

    distance_tutup = (TimeElapsed * 34300) / 2

    return distance_tutup


def distance_dalam():
    GPIO.output(GPIO_trig2, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_trig2, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_echo2) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_echo2) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime

    distance_dalam = (TimeElapsed * 34300) / 2

    return distance_dalam


def distance_jalan():
    GPIO.output(GPIO_trig3, True)

    time.sleep(0.00001)
    GPIO.output(GPIO_trig3, False)

    StartTime = time.time()
    StopTime = time.time()

    while GPIO.input(GPIO_echo3) == 0:
        StartTime = time.time()

    while GPIO.input(GPIO_echo3) == 1:
        StopTime = time.time()

    TimeElapsed = StopTime - StartTime

    distance_jalan = (TimeElapsed * 34300) / 2

    return distance_jalan


if __name__ == '__main__':
    try:
        while True:
            hasil_distance_tutup = distance_tutup()
            hasil_distance_jalan = distance_jalan()
            hasil_distance_dalam = distance_dalam()
            if hasil_distance_dalam > 10:
                if hasil_distance_tutup < 50:
                    #pservo = GPIO.PWM(GPIO_servo, 50)
                    pservo.start(2.5)
                    print("Tong sampah membuka.")
                    pservo.ChangeDutyCycle(12)
                    time.sleep(5)
                    os.system('mpg321 bin.mp3 &')
                    time.sleep(3)
                    os.system('mpg321 bin2.mp3 &')
                    time.sleep(3)
                    pservo.ChangeDutyCycle(2.5)
                    #time.sleep(2)
                    #pservo.stop(2.5)
            else:
                if hasil_distance_jalan < 20:
                    GPIO.output(GPIO_drivein1, GPIO.LOW)
                    GPIO.output(GPIO_drivein2, GPIO.LOW)
                    GPIO.output(GPIO_drivein3, GPIO.LOW)
                    GPIO.output(GPIO_drivein4, GPIO.LOW)
                    #print("[Diam]")
                else:
                    if not GPIO.input(GPIO_center):
                        GPIO.output(GPIO_drivein1, GPIO.HIGH)
                        GPIO.output(GPIO_drivein2, GPIO.LOW)
                        GPIO.output(GPIO_drivein3, GPIO.HIGH)
                        GPIO.output(GPIO_drivein4, GPIO.LOW)
                        #print("[SUDAH PENUH] Tong sampah jalan lurus")
                    elif not GPIO.input(GPIO_left):  # belok kanan
                        GPIO.output(GPIO_drivein1, GPIO.HIGH)
                        GPIO.output(GPIO_drivein2, GPIO.LOW)
                        GPIO.output(GPIO_drivein3, GPIO.LOW)
                        GPIO.output(GPIO_drivein4, GPIO.HIGH)
                        #print("[SUDAH PENUH] Tong sampah belok ke kanan")
                    elif not GPIO.input(GPIO_right):  # belok kiri
                        GPIO.output(GPIO_drivein1, GPIO.LOW)
                        GPIO.output(GPIO_drivein2, GPIO.HIGH)
                        GPIO.output(GPIO_drivein3, GPIO.HIGH)
                        GPIO.output(GPIO_drivein4, GPIO.LOW)
                        #print("[SUDAH PENUH] Tong sampah belok ke kiri")
                    else:  # tidak mendeteksi apapun(diam)
                        GPIO.output(GPIO_drivein1, GPIO.LOW)
                        GPIO.output(GPIO_drivein2, GPIO.LOW)
                        GPIO.output(GPIO_drivein3, GPIO.LOW)
                        GPIO.output(GPIO_drivein4, GPIO.LOW)
                        #print("[SUDAH PENUH] Line Tidak Terdeteksi(DIAM)")

    except KeyboardInterrupt:
        print("Error")
        GPIO.cleanup()