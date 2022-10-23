const Gpio = require('pigpio').Gpio; //https://github.com/fivdi/pigpio
var sleep = require('sleep'); //https://www.npmjs.com/package/sleep
var player = require('play-sound')(opts = {}) //https://www.npmjs.com/package/play-sound

// The number of microseconds it takes sound to travel 1cm at 20 degrees celcius
const MICROSECDONDS_PER_CM = 1e6/34321;

const trigger1 = new Gpio(2, {mode: Gpio.OUTPUT});
const trigger2 = new Gpio(14, {mode: Gpio.OUTPUT});
const trigger3 = new Gpio(23, {mode: Gpio.OUTPUT});
const echo1 = new Gpio(3, {mode: Gpio.INPUT, alert: true});
const echo2 = new Gpio(15, {mode: Gpio.INPUT, alert: true});
const echo3 = new Gpio(24, {mode: Gpio.INPUT, alert: true});
const servo = new Gpio(21, {mode: Gpio.OUTPUT});
const right = new Gpio(11, {mode: Gpio.INPUT});
const left = new Gpio(9, {mode: Gpio.INPUT});
const center = new Gpio(10, {mode: Gpio.INPUT});
const drive1 = new Gpio(5, {mode: Gpio.OUTPUT});
const drive2 = new Gpio(6, {mode: Gpio.OUTPUT});
const drive3 = new Gpio(19, {mode: Gpio.OUTPUT});
const drive4 = new Gpio(26, {mode: Gpio.OUTPUT});

trigger1.digitalWrite(0); // Make sure trigger is low
trigger2.digitalWrite(0); // Make sure trigger is low
trigger3.digitalWrite(0); // Make sure trigger is low

const watchHCSR04 = () => {
    let startTick1;
    let startTick2;
    let startTick3;

echo1.on('alert', (level1, tick1) => {
    if (level1 == 1) {
      startTick1 = tick1;
    } else {
      const endTick1 = tick1;
      const diff1 = (endTick1 >> 0) - (startTick1 >> 0); // Unsigned 32 bit arithmetic
      const distance1 = diff1 / 2 / MICROSECDONDS_PER_CM;
      console.log("Sensor 1 :", distance1);
      if (distance1 < 50) {
        console.log('tong buka');
        servo.servoWrite(2500);
        sleep.sleep(5);
        player.play('bin.mp3', function (err) {
          if (err) throw err;
          console.log("Audio finished");
        });
        sleep.sleep(3)
        player.play('bin2.mp3', function (err) {
          if (err) throw err;
          console.log("Audio finished");
        });
        sleep.sleep(3)
        servo.servoWrite(500);
        sleep.sleep(1);
        servo.servoWrite(0);
      }
    }
});

echo2.on('alert', (level2, tick2) => {
    if (level2 == 1) {
        startTick2 = tick2;
    } else {
        const endTick2 = tick2;
        const diff2 = (endTick2 >> 0) - (startTick2 >> 0); // Unsigned 32 bit arithmetic
        const distance2 = diff2 / 2 / MICROSECDONDS_PER_CM;
        console.log("Sensor 2 :", distance2);
        if (distance2 < 10){
            console.log('penuh');
            echo3.on('alert', (level3, tick3) => {
                if (level3 == 1) {
                    startTick3 = tick3;
                } else {
                    const endTick3 = tick3;
                    const diff3 = (endTick3 >> 0) - (startTick3 >> 0); // Unsigned 32 bit arithmetic
                    const distance3 = diff3 / 2 / MICROSECDONDS_PER_CM;
                    console.log("Sensor 3 :", distance3);
                    const kanan = right.digitalRead();
                    const kiri = left.digitalRead();
                    const tengah = center.digitalRead();
                    if(distance3 < 20){
                    drive1.digitalWrite(0);
                    drive2.digitalWrite(0);
                    drive3.digitalWrite(0);
                    drive4.digitalWrite(0);
                    console.log("berhenti");
                    } else {
                    if(kanan == 0){
                        drive1.digitalWrite(1);
                        drive2.digitalWrite(0);
                        drive3.digitalWrite(0);
                        drive4.digitalWrite(1);
                        console.log("kanan");
                    } else if(kiri == 0){
                        drive1.digitalWrite(0);
                        drive2.digitalWrite(1);
                        drive3.digitalWrite(1);
                        drive4.digitalWrite(0);
                        console.log("kiri");
                    } else if(tengah == 0){
                        drive1.digitalWrite(1);
                        drive2.digitalWrite(0);
                        drive3.digitalWrite(1);
                        drive4.digitalWrite(0);
                        console.log("lurus");
                    } else {
                        drive1.digitalWrite(0);
                        drive2.digitalWrite(0);
                        drive3.digitalWrite(0);
                        drive4.digitalWrite(0);
                        console.log("Tidak ada garis");
                    }
                }
            }
        });
        } else {
            //echo3.off;
            drive1.digitalWrite(0);
            drive2.digitalWrite(0);
            drive3.digitalWrite(0);
            drive4.digitalWrite(0);
            console.log("tong belum penuh");
        }
            }
        });

};

watchHCSR04();

// Trigger a distance measurement once per second
setInterval(() => {
  trigger1.trigger(10, 1); // Set trigger high for 10 microseconds
  trigger2.trigger(10, 1); // Set trigger high for 10 microseconds
  trigger3.trigger(10, 1); // Set trigger high for 10 microseconds
}, 1000);