import json
import logging
import struct

from channels import Group
from django.core.management.base import BaseCommand
from paho.mqtt import client as mqtt
from paho.mqtt.client import MQTTMessage

from apps.tracking import models

logger = logging.getLogger('tracking.position')


class Command(BaseCommand):
    help = 'Subscribe to MQTT broker'

    def handle(self, *args, **options):
        Group("tracking").send({"text": json.dumps({'lat': 11, 'lng': 22})}, immediately=True)
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        client.connect("127.0.0.1", 1883, 60)

        try:
            client.loop_forever()
        except KeyboardInterrupt:
            client.disconnect()
            logger.info('DISCONNECTED FROM BROKER')


def on_connect(client, userdata, flags, rc):
    logger.info('CONNECTED TO BROKER')
    client.subscribe("tracking/positions")


def on_message(client, userdata, msg: MQTTMessage):
    payload = list(msg.payload)
    lat, = struct.unpack('!d', bytes(payload[0:8]))
    lng, = struct.unpack('!d', bytes(payload[9:17]))

    device = models.Device.objects.get(serial_number='12345')
    position = models.Position.objects.create(lat=lat, lng=lng, device=device)

    logger.info('POSITION RECEIVED: (%s, %s)', lat, lng)

    Group("tracking").send({"text": json.dumps({'lat': lat, 'lng': lng})}, immediately=True)
