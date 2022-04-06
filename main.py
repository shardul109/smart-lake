from src.db.models import init_db
from src.devices.common import init_devices

if __name__ == '__main__':
    init_db()
    init_devices()
