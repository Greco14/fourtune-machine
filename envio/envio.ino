#include <SPI.h>         // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>     // UDP library from: bjoern@cs.stanford.edu 12/30/2008

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress server(66, 228, 50, 204);
IPAddress address(192, 168, 1, 201);
unsigned int port = 2323, packetSize, checkin, secs = 5000; // UDP port on server

// Buffer to hold incoming packet
char packetBuffer[UDP_TX_PACKET_MAX_SIZE], command[] = "c";

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;
int motor = 3;// The pin for the motor to use

void setup() 
{
  // Request DHCP for address or use default
  if (Ethernet.begin(mac)) {
    Serial.print("Obtenida IP: ");
    Serial.println(Ethernet.localIP());
  } else {
    Ethernet.begin(mac, address);
  }
    
  Udp.begin(port);
  Serial.begin(9600);
  
  // Set the motor PIN
  pinMode(motor,OUTPUT);
}

void loop()
{
  // Send a request for checkin status on our
  // UDP server
  Serial.println ("Sending request...");
  Udp.beginPacket(server, port);
  Udp.write(command);
  Udp.endPacket();
    
  int packetSize = Udp.parsePacket();
     
  if (packetSize) {
    IPAddress remote = Udp.remoteIP();
    // Read the packet into packetBufffer
    Udp.read(packetBuffer,UDP_TX_PACKET_MAX_SIZE);
    Serial.println("Recived: ");
    Serial.println(packetBuffer);
    checkin = atoi(packetBuffer);  
    
    // Activate the motor if we have a checkin
    if (checkin == 1) {
      Serial.println("Activating the motor");
      digitalWrite(motor, HIGH);
      delay(1000);
      digitalWrite(motor, LOW);
    } 
  }
  
  delay(secs);
}

