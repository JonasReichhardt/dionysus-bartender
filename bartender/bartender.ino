
#define in1 2
#define in2 3

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
    digitalWrite(in1,LOW);
  digitalWrite(in2,LOW);
}

// the loop function runs over and over again forever
void loop() {

  digitalWrite(in1, HIGH);   // turn the left pump on (HIGH is the voltage level)
  delay(1000);                       // wait for a second
  digitalWrite(in1, LOW);    // turn the left pump off by making the voltage LOW
  delay(1000);                       // wait for a second
}
