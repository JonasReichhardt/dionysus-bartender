#define pin1 8
#define pin2 9
#define pin3 10
#define pin4 11
#define pin5 12
#define pin6 13

unsigned long starts[6];
long waitTimes[6];
bool setFlags[] = {false,false,false,false,false,false};
int pins[] = {pin1,pin2,pin3,pin4,pin5,pin6};

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 6; i = i + 1) {
    pinMode(pins[i], OUTPUT);
  }
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB
  }
}

void loop() {
  update_pins();
  check_for_input();
}

void update_pins(){
  unsigned long cur_millis = millis();

  for (int i = 0; i < 6; i = i + 1) {
    if((cur_millis - starts[i]) >= waitTimes[i] && setFlags[i]){
      setFlags[i] = false;
      digitalWrite(pins[i],LOW);
    }
  }
}

void check_for_input(){
  if (Serial.available() > 0) {
    long data = Serial.parseInt(SKIP_NONE);

    // last two digits indicate pin    
    int pin = data % 100;
    data = data / 100;

    int index = -1;
    for (int i = 0; i < 6; i = i + 1) {
      if(pin == pins[i]){
        index = i;
      }
    }

    // pin not found -> return
    if(index == -1){
      return;
    }

    setFlags[index] = true;
    waitTimes[index] = data;
    starts[index] = millis();
    digitalWrite(pins[index],HIGH);
  }
}
