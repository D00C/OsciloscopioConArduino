# OsciloscopioConArduino
La estructura del directorio es la siguiente:
* Un directorio /documentación que incluye el reporte del proyecto en Latex y en pdf, un
  subdirectorio /documentación/figuras donde se incluyen tanto las imágenes usadas para el
  reporte como las usadas en la presentación y un subdirectorio
  /documentación/presentación con el archivo de la presentación en Latex y en pdf.
* Un directorio /codigo con un subdirectorio /codigo/ReadAnalogVoltage que contiene el
  archivo ReadAnalogVoltage.ino que es el código ejemplo de Arduino para leer voltaje
  desde uno de los puertos analógicos, solo se le modifico un parámetro especificado en
  los comentarios del código y se hizo la traducción de los comentarios para la
  documentación, también se incluye el archivo /codigo/osciloscopio.py que contiene el
  código en python para utilizar los datos que proporciona Arduino en una gráfica en
  tiempo real.
