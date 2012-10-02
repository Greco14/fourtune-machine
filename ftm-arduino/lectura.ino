int 
lecturaCO(int analogPin)
{
  int lecturaRaw = 0;
  int voltajeRaw = 0; 
  
  Serial.println("Tomando lectura de CO...");
  
  lecturaRaw = analogRead(analogPin);
  voltajeRaw = lecturaRaw * 5/1024;
  
  Serial.print("Lectura: ");
  Serial.print(lecturaRaw);
  Serial.print("\n");
  Serial.print("Voltaje: ");
  Serial.print(voltajeRaw);
  Serial.print("\n");
 
  return lecturaRaw;
}
