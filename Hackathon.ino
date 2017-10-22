#include <Stepper.h>

int t =0;
const int stepsPerRevolution = 200;  // change this to fit the number of steps per revolution
// for your motor


// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8, 9, 10, 11);

int stepCount = 0;  // number of steps the motor has taken

char controlState = 'S';
int controlVariable1 = 255;


void setup() {
  Serial.begin(115200);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop() {

  if(Serial.available()){

      //int i = Serial.parseInt();
      int i = Serial.read();
//      if(i>5 || i<250){
        Serial.println(i);
        if(i>127){
          //clockwise state
          myStepper.setSpeed(175);
          // step 1/100 of a revolution:
          myStepper.step(5);
        }else{
        
            //counterclockwise state
            myStepper.setSpeed(175);
            // step 1/100 of a revolution:
            myStepper.step(-5);
        }
//      }
      
      while(Serial.available()){
        Serial.read();
      }
  }
  

  
}
