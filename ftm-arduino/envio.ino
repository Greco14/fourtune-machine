byte server[] = {192,168,1,109};
unsigned int port = 8080;

void 
enviar(int lectura, boolean init)
{
  String msj;
  
  String host = "Host: ";
  host.concat(Ethernet.localIP());
  
  msj = hacerMensaje(lectura, init);
  /* Serial.println(msj); */
  
  delay(1000);
  
  Serial.println("Connectado al servidor...");
  if (client.connect(server, port)) {  
    client.println("POST /hola HTTP/1.1");
    client.println(host);
    client.println("Content-Type: application/x-www-form-urlencoded");
    client.println("Connection: close");
    client.print("Content-Length: ");
    client.println(msj.length());
    client.println();
    client.print(msj);
    client.println();
    
    Serial.print("Mensaje enviado : <");
    Serial.print(msj);
    Serial.println(">");
    Serial.println();
    
    delay(1000);
    
    manejarRespuesta();
  } else {
    Serial.println("Conexion fallo...");
  }
  
  client.stop();
}

String 
hacerMensaje(int lectura, boolean init)
{
  String msj;
  
  if (init) {
    msj = "Status = initConexion";
  } else {
    msj = "dato=";
    msj.concat(String(lectura));
  }
  
  return msj; 
}

void 
manejarRespuesta()
{
  while (client.available()) {
    char c = client.read();
    Serial.print(c);
  }
}
