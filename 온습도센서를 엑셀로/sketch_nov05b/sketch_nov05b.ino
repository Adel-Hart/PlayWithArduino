#include <DHT11.h>
#define dhta 8 //온습도 센서
#define echo 6 //필요X
#define trig 7 // 필요 X

DHT11 dht(dhta);

float temp, humi;

void setup() {
  // put your setup code here, to run once:
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  long distance, duration
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);

  distance = duration * 17 / 1000;

  
  dht.read(humi, temp);
  Serial.print(humi);
  Serial.print(", ");
  Serial.print(temp);
  Serial.print(", ");
  Serial.println(DHT11_RETRY_DELAY);

  delay(DHT11_RETRY_DELAY);
}
