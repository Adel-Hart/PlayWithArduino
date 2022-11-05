#define echo 6
#define trig 7

long setTer;

int flag;

void setup() {
  // put your setup code here, to run once:
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  char what;
  // put your main code here, to run repeatedly:
  long duration, distance;
  
  digitalWrite(trig, LOW);
  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);

  distance = duration * 17 / 1000;

  what = Serial.read();

  
    
  
  switch(what){
    case 's':
      setTer = distance;
      Serial.println("Set complete");
      break;
     case 'g':
      flag = 1;
      Serial.println("Start");
      break;
     case 'n':
      flag = 0;
      Serial.println("Done");
      break;
     default:
      break;
        
  }
  
  if(flag == 1){
    if(setTer - 2 > distance){
      Serial.println("BOOM");
    }
  }

  delay(100);
}
