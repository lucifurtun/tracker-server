from time import sleep

from paho.mqtt import client as mqtt
import struct

client = mqtt.Client()
client.connect("127.0.0.1", 1883, 60)

SIMPLE_ROAD = ((45.747924, 21.225583), (45.747880, 21.225870), (45.747835, 21.226327), (45.747761, 21.226932),
               (45.747732, 21.227622), (45.747747, 21.228238), (45.747776, 21.228992), (45.747858, 21.229947),
               (45.747924, 21.230691), (45.748021, 21.231445), (45.748147, 21.232220), (45.748339, 21.233674))


def main():
    for point in SIMPLE_ROAD:
        lat, lng = point
        payload = _get_payload(lat, lng)

        client.publish('tracking/positions', bytearray(payload))

        sleep(1)

    client.disconnect()


def _get_payload(lat, lng):
    payload = list()

    payload += list(struct.pack('!d', lat))
    payload += list(struct.pack('c', b':'))
    payload += list(struct.pack('!d', lng))

    return bytearray(payload)


if __name__ == '__main__':
    main()
