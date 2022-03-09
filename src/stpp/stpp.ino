#define pin1 8
#define pin2 9
#define pin3 10
#define pin4 11
#define pin5 12
#define pin6 13

#define DEBUG false

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
  for (int i = 0; i < 6; i = i + 1) {
    if(setFlags[i]){
      if(millis() - starts[i] >= waitTimes[i] ){
        #if DEBUG
          Serial.print(pins[i],DEC);
          Serial.print(":");
          Serial.println(millis() - starts[i]);
    	  #endif
        setFlags[i] = false;
        digitalWrite(pins[i],LOW);
      }
    }
  }
}

void check_for_input(){
  if (Serial.available() > 0) {
    long data = Serial.parseInt(SKIP_NONE);

    // last digit = index of pump array   
    int index = data % 10;
    data = data / 10;

    setFlags[index] = true;
    waitTimes[index] = data;
    starts[index] = millis();
    digitalWrite(pins[index],HIGH);
    #if DEBUG
        Serial.print(pins[index],DEC);
        Serial.print(":");
        Serial.println(data,DEC);
    #endif
  }
}
