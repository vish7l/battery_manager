bool ledOn = false;

void setup() {
  pinMode(13, OUTPUT);  // Set pin 13 as an output
  Serial.begin(9600);   // Start serial communication at 9600 bps
}

void loop() {
  if (Serial.available()) {  // If data is available to read
    String data = Serial.readString();  // Read the data
    if (data == "80" && !ledOn) {  // If the data is "80" and the LED is not already on
      digitalWrite(13, HIGH);  // Turn on the LED
      ledOn = true;  // Set the flag to indicate the LED is on
    }
  }
}
