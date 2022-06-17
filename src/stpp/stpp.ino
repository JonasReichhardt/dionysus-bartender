#include <HX711_ADC.h>

#define pin1 49
#define pin2 53
#define pin3 44
#define pin4 42
#define pin5 48
#define pin6 52

#define pin1r 47
#define pin2r 51
#define pin3r 45
#define pin4r 43
#define pin5r 46
#define pin6r 50

// preprocessor options
#define DEBUG_UPDATE_PINS false
#define DEBUG_CHECK_INPUT false
#define PRINT_READY_MSG true
#define DEBUG_RESET false
#define DEBUG_WEIGHT false

#define PUMP_DELAY 3000
#define NUM_OF_PUMPS 6

#define CAL_FACTOR -1058.28
#define WEIGHT_THRESHOLD 100.0

HX711_ADC LoadCell(22, 23);
unsigned long endTimes[6];
bool setFlags[] = {false,false,false,false,false,false};
int pins[] = {pin1,pin2,pin3,pin4,pin5,pin6};
int rPins[] = {pin1r,pin2r,pin3r,pin4r,pin5r,pin6r};

void setup() {
  Serial.begin(115200);
  LoadCell.begin();
  LoadCell.setCalFactor(CAL_FACTOR);
  LoadCell.start(2000);
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
  LoadCell.update();
  update_pins();
  check_for_input();
}

void update_pins(){
  for (int i = 0; i < 6; i = i + 1) {
    if(setFlags[i]){
      if(millis() >= endTimes[i] || !weightThresholdExceeded()){
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

bool weightThresholdExceeded() {
  // load current weight on scale
  float i = LoadCell.getData();
  #if DEBUG_WEIGHT
    Serial.print("Load_cell output val: ");
    Serial.println(i);
  #endif
  
  // return true if measured weight exceeds threshold
  return i > WEIGHT_THRESHOLD;
}

void check_for_input(){
  // cancel cocktail
  if(Serial.peek()=='x'){
    reset();
    Serial.read();
    return;
  } else if(Serial.peek() == 'e') {
    Serial.print('e');
    Serial.read();
    emptyTubes();
    return;
  }
  
  // check for new input
  if (Serial.available() > 10 && weightThresholdExceeded()) {
    for(int i=0; i < NUM_OF_PUMPS; i=i+1){
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
  } else if(Serial.available() > 10 && !weightThresholdExceeded()) {
    serialFlush();
    #if DEBUG_WEIGHT
      Serial.println("Serial data flushed");
    #endif
  }
}

void serialFlush(){
  while(Serial.available() > 0) {
    char t = Serial.read();
  }
}

void emptyTubes() {
  // start clearing the tubes
  for (int i = 0; i < NUM_OF_PUMPS; i++) {
    digitalWrite(rPins[i], HIGH);
  }

  // wait for 3 seconds
  delay(PUMP_DELAY);

  // stop rotating the pumps
  for (int i = 0; i < NUM_OF_PUMPS; i++) {
    digitalWrite(rPins[i], LOW);
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
