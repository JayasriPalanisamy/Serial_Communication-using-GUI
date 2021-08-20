/*
 * Hello World!
 *
 * This is the Hello World! for Arduino. 
 * It shows how to send data to the computer
 */


void setup()                    // run once, when the sketch starts
{
  Serial.begin(9600);           // set up Serial library at 9600 bps
  
 // Serial.println("Hello world!");  // prints hello with ending line break 
}
unsigned int count=0;
void loop()                       // run over and over again
{

  delay(1000);
     Serial.println(count); 
     if(count>9)
     {
       count=0;
     }
     count++;
}
