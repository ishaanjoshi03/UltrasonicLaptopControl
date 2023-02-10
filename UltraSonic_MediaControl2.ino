const int trigger1 = 13; //Trigger pin of 1st Sesnor
const int echo1 = 12; //Echo pin of 1st Sesnor

long time_taken;
int dist,distL;

void setup() {
Serial.begin(9600); 
  
pinMode(trigger1, OUTPUT); 
pinMode(echo1, INPUT); 
}

/*###Function to calculate distance###*/
void calculate_distance(int trigger, int echo)
{
digitalWrite(trigger, LOW);
delayMicroseconds(2);
digitalWrite(trigger, HIGH);
delayMicroseconds(10);
digitalWrite(trigger, LOW);

time_taken = pulseIn(echo, HIGH);
dist= time_taken*0.034/2;
}
void loop() {
calculate_distance(trigger1,echo1);
distL =dist; //get distance of left sensor

if (distL >60 && distL<70) { //Detect Left Hand
Serial.println("Rewind"); delay (500);
}

//Uncomment for debudding
/*Serial.print("L=");
Serial.println(distL);
Serial.print("R=");
Serial.println(distR);
*/

calculate_distance(trigger1,echo1);
distL =dist;

//Control Modes
//Lock Left - Control Mode
if (distL>=25 && distL<=35) {
  delay(100); //Hand Hold Time
  calculate_distance(trigger1,echo1);
  distL = dist;
  if (distL>=25 && distL<=35)
  {
    Serial.println("Left Locked");
    while(distL<=60)
    {
      calculate_distance(trigger1,echo1);
      distL =dist;
      while (distL<20) { //Hand pushed in
        Serial.println ("Vup"); delay (300);
        calculate_distance(trigger1,echo1);
        distL =dist;
      }
      while (distL>40 and distL < 60) {//Hand pulled out
        Serial.println ("Vdown"); delay (300);
        calculate_distance(trigger1,echo1);
        distL = dist;
      }
    }
  }
}

delay(200);
}
