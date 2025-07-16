#include <DHT.h>  //DHT libraries
#include <DHT_U.h>
#define Type DHT11

const int sensePin = 3;
DHT HT(sensePin, Type);

float humid; // DHT vars
float tempC;
float tempF;

const int readPin = A0;
int sensorValue;
float volts;
float lr; // Light rating, measured form voltage of photoresistor

float env_s; // Enviornmental score, average of all other values

void setup() {
  
  pinMode(readPin, INPUT); // Voltage divider pin setup


  Serial.begin(9600);// DHT sensor setup and Serial monitor setup
  HT.begin();

}

void loop() {

  humid = HT.readHumidity(); // Getting data from DHT and stroing it into vars
  tempC = HT.readTemperature();
  tempF = (9/5) * tempC + 32;  // Converting from celcius to farenheit
  
  Serial.print("Temperature: ");  // Printing DHT values to the Serial Monitor
  Serial.print(tempF);
  Serial.print(", Humidity: ");
  Serial.print(humid);

  sensorValue = analogRead(readPin); // Reading input from voltage divider circuit
  volts = sensorValue * (5.0/1024.0); // Converting input to voltage

  lr = volts / 10 ;  // "Rating" voltage from 0 - 0.5

  Serial.print(", Light Rating: "); // Printing Light rating to serial monitor
  Serial.println(lr);

  env_s = ( humid + tempF + lr ) / 3;

  Serial.print("Enviornmental Score: ");
  Serial.println(env_s);


  delay(1000);

}
