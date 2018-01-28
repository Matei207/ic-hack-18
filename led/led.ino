int ledPin;

void setup() {
  pinMode(4, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  Serial.begin(9600);
}

void loop() {
   if (Serial.available()){
     ledPin = Serial.read() - '0';
     Serial.println(ledPin);
     light(ledPin);
   }
   delay(500);
}

void light(int pin){
  digitalWrite(pin, HIGH);
  delay(1000);
  digitalWrite(pin, LOW);
  delay(1000);
}
