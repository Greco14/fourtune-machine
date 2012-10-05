#include <SPI.h>         // needed for Arduino versions later than 0018
#include <Ethernet.h>
#include <EthernetUdp.h>     // UDP library from: bjoern@cs.stanford.edu 12/30/2008


// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {  
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress remoteIp(66, 228, 50, 204);
IPAddress localIp(192, 168, 1, 201);

unsigned int localPort = 2323;      // local port to listen on

// buffers for receiving and sending data
char packetBuffer[UDP_TX_PACKET_MAX_SIZE]; //buffer to hold incoming packet,
char  ReplyBuffer[] = "c" ;      

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;
int motor=3;

void setup() {
  // start the Ethernet and UDP:
  Ethernet.begin(mac,localIp);
  Udp.begin(localPort);
  Serial.begin(9600);
  
  pinMode(motor,OUTPUT);
}

void loop() {
  // if there's data available, read a packet
  Serial.println ("iniciando envio de paquete");
    Udp.beginPacket(remoteIp, localPort);
    Udp.write(ReplyBuffer);
    Udp.endPacket();
    
   int packetSize = Udp.parsePacket();
     
  if(packetSize)
  {
    Serial.print("Received packet of size ");
    Serial.println(packetSize);
    Serial.print("From ");
    IPAddress remote = Udp.remoteIP();
    for (int i =0; i < 4; i++)
    {
      Serial.print(remote[i], DEC);
      if (i < 3)
      {
        Serial.print(".");
      }
    }
    Serial.print(", port ");
    Serial.println(Udp.remotePort());

    // read the packet into packetBufffer
    Udp.read(packetBuffer,UDP_TX_PACKET_MAX_SIZE);
    Serial.println( );
    Serial.println(packetBuffer);

    // send a reply, to the IP address and port that sent us the packet we received
   if (Serial.available() > 0) {

       digitalWrite(motor, HIGH);
   }else{
        digitalWrite(motor, LOW);
   }          
      
  }
  delay(1000);
}

