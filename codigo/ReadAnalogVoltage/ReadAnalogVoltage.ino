/*
  Ejemplo para leer el voltaje análogo encontrado en el archivo de ejemplos de Arduino,
  solo se cambio los bits por segundo de 9600 a 115200 debido a que se noto una mejor
  respuesta del osciloscopio con esto durante las pruebas y se hizo la traducción de los
  comentarios para la documentación
  El código del ejemplo original esta en:
  http://www.arduino.cc/en/Tutorial/ReadAnalogVoltage
*/

// El siguiente código corre cuando se presiona el botón de reinicio
void setup() {
  // Iniciar la comunicación con el puerto serial a 115200 bits por segundo
  Serial.begin(115200);
}

// El siguiente código corre infinitamente
void loop() {
  // Leer el valor de entrada del puerto A0
  int sensorValue = analogRead(A0);
  // Convertir el valor de entrada (Que va de 0 - 1023) a un voltaje (De 0 - 5v)
  float voltage = sensorValue * (5.0 / 1023.0);
  // Imprimir el voltaje leído en el puerto serial
  Serial.println(voltage);
  delay(10);
}
