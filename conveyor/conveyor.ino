void setup() {
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  Serial.begin(9600);
}

void loop() {
   digitalWrite(3, HIGH);
   digitalWrite(4, HIGH);
   analogWrite(9, 200);
}
