import paho.mqtt.client as mqtt
topic = "deviceid/Yun/evt/light"
topic_relay = "deviceid/Yuning/cmd/lamp"
server = "52.4.159.58"

def on_connect(client, userdata, flags, rc):
    print("Connected with RC : " + str(rc))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    print(msg.topic + " " +str(msg.payload.decode('UTF-8')))

    if int(msg.payload) > 300:
        client.publish(topic_relay, "on")
    else:
        client.publish(topic_relay, "off")

client = mqtt.Client()
client.connect(server, 1883,60)
client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
