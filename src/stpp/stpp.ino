#define pin1 22
#define pin2 23
#define pin3 24
#define pin4 25
#define pin5 26
#define pin6 27

// preprocessor options
#define DEBUG_UPDATE_PINS false
#define DEBUG_CHECK_INPUT false
#define PRINT_READY_MSG true
#define DEBUG_RESET false

unsigned long endTimes[6];
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
  #if PRINT_READY_MSG
    Serial.println("RDY");
  #endif
}

void loop() {
  update_pins();
  check_for_input();
}

void update_pins(){
  for (int i = 0; i < 6; i = i + 1) {
    if(setFlags[i]){
      if(millis() >= endTimes[i]){
        #if DEBUG_UPDATE_PINS
          Serial.print(i,DEC);
          Serial.println(":LOW");
    	  #endif
        setFlags[i] = false;
        digitalWrite(pins[i],LOW);
      }
    }
  }
}

void check_for_input(){
  // cancel cocktail
  if(Serial.peek()=='x'){
    reset();
    Serial.read();
    return;
  }

  // check for new input
  if (Serial.available() > 10) {
    for(int i=0; i<6; i=i+1){
      long data = Serial.parseInt();
      
      if(data > 0 && !setFlags[i]){
        setFlags[i] = true;
        endTimes[i] = millis()+data;
        digitalWrite(pins[i],HIGH);
        
        #if DEBUG_CHECK_INPUT
            Serial.print(i,DEC);
            Serial.print(":");
            Serial.println(data,DEC);
        #endif
      }
    }
    // remove last byte from buffer
    Serial.read();
  }
}

void reset(){
  for(int i=0; i<6; i=i+1){
    digitalWrite(pins[i],LOW);
    setFlags[i] = false;
  }
  #if DEBUG_RESET
    Serial.println("RESET");
  #endif
}
