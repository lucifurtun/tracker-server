import logging

from django.core.management.base import BaseCommand
from paho.mqtt import client as mqtt
from paho.mqtt.client import MQTTMessage

from apps.tracking import models

logger = logging.getLogger('tracking.position')


class Command(BaseCommand):
    help = 'Subscribe to MQTT broker'

    def handle(self, *args, **options):
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
    device = models.Device.objects.get(serial_number='12345')
    position = models.Position.objects.create(lat=45.7494493, lng=21.2312252, device=device)

    logger.info('POSITION RECEIVED: (%s, %s)', position.lat, position.lng)
