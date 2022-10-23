# SMARTBIN

Code ini dibuat untuk raspberry-pi menggunakan pin GPIO untuk menjalankan fungsi tong sampah otomatis


<p align="center">

  <img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E" />

  <img src="https://img.shields.io/badge/node.js%20-%2343853D.svg?&style=for-the-badge&logo=node.js&logoColor=white" />

  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />

</p>

---------

### Hardware & Software 

- Raspberry 3/4
- 3x Sensor HC-SR04
- 3x Sensor TRCT5050 (line tracer)
- 1 Servo MG995
- 2x Driver Motor (L298N)
- 4x Motor DC high torque
- [`NodeJs`](https://nodejs.org/en/) support Version : 12, 13, 14, 15, 16
- [`Python`](https://www.python.org/downloads/)
- RPi.GPIO : [`Python`](https://pypi.org/project/RPi.GPIO/)  
- pigpio   : [`NpmJs`](https://github.com/fivdi/pigpio)

---------

## Script:

<p align="left">

  ➛ <a href="https://github.com/TierKun/Telegram-Bot-IoT">Python</a>

</p>

<p align="left">

  ➛ <a href="https://github.com/TierKun/Whatsapp-Bot-IoT">JavaScript</a>

</p>



---------



### Installation


* [`Driver CH34x For NodeMcu lolin`](https://github.com/TierKun/IoT-Relay/blob/main/Driver%20%26%20Library/CH341SER.zip)

* [`Library ESP8266`](https://github.com/TierKun/IoT-Relay/blob/main/Driver%20%26%20Library/ESP8266wifi-master.zip)

* [`Library Blynk`](https://github.com/TierKun/IoT-Relay/blob/main/Driver%20%26%20Library/blynk-library-master.zip)

* [`Driver&Tools Flash Error`](https://github.com/TierKun/IoT-Relay/blob/main/Driver%20%26%20Library/Flash%20NODEmcu.rar)



---------

#### Edit Config Token Server Blynk

<p align="left">

  ‣ <a href="https://github.com/TierKun/IoT-Relay/blob/main/Code/IoT%20Relays.ino#L16-L18">Edit Token Config</a>

</p>



```C++



#define BLYNK_TEMPLATE_ID "ISI_TEMPLATE_ID"

#define BLYNK_DEVICE_NAME "NAMA_DEVICE"

#define BLYNK_AUTH_TOKEN "ISI_TOKEN"



```

---------



#### Edit Wifi Config



<p align="left">

   ‣ <a href="https://github.com/TierKun/IoT-Relay/blob/main/Code/IoT%20Relays.ino#L22-L23">Edit Wifi Config</a>

</p>



```C++



char ssid[] = "sinyo";//Masukkan Nama Wifi/SSID

char pass[] = "sukasukasaya";//Masukkan WIFI password



```



---------
