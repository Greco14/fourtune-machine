#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0x90, 0xA2, 0xDA, 0x00, 0x82, 0x83 };
EthernetClient client;

void 
setup()
{
  boolean hasIP = false;
  
  /* launch dhcp */
  if (Ethernet.begin(mac))
     hasIP = true;
   
  Serial.begin(9600);
  delay(1000);
  
  Serial.println("Version : 0006");
  Serial.println("Iniciando . . .");
  
  if (hasIP) {
    Serial.print("Obtenida IP: ");
    Serial.println(Ethernet.localIP());
  } else {
    while (hasIP == false) {
      Serial.print("Obteniendo IP...");
      
      if (Ethernet.begin(mac)) {
        Serial.print("Obtenida IP: ");
        Serial.println(Ethernet.localIP());
        
        hasIP = true;
      }
        
      delay(1000);
    }
  }
  
  Serial.println("");
  Serial.println("Enviando inicializacion...");
  enviar(0, true);
  Serial.println("");
}

void loop()
{
   int lectura = 0;
   
   lectura = lecturaCO(0);
   
   Serial.println("Enviando mensaje...");
   enviar(lectura, false);
   
   Serial.println("");
   
   delay(1000);
}
