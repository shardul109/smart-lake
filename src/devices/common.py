import datetime
from src.devices.dht11 import dht11
from src.db.models import DeviceValues, get_session
from sqlalchemy.orm.session import Session
from time import sleep
import paho.mqtt.client as mqtt


def init_devices():
    while True:
        db: Session = get_session()
        time = datetime.datetime.now()
        temp, hum = dht11()

        new_entry = DeviceValues(
            temperature=temp,
            humidity=hum,
            time=time
        )
        db.add(new_entry)
        db.commit()

        client = mqtt.Client()
        client.connect("localhost", 1883, 60)
        client.publish("topic/test", new_entry)
        client.disconnect()

        sleep(1 * 60)
