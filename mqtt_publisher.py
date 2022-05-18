import paho.mqtt.publish as publish
import Adafruit_DHT

MQTT_SERVER = "localhost"
MQTT_PATH = "temp"
while True:
    humidity, temperature = Adafruit_DHT.read_retry(11, 27)  # GPIO27 (BCM notation)
    print ("Humidity = {} %; Temperature = {} C".format(humidity, temperature))
    publish.single(MQTT_PATH, format(temperature), hostname=MQTT_SERVER)

