from dataclasses import dataclass

import msgspec
from faststream.rabbit import RabbitBroker

from app.application.dto import YoloProcessDto
from app.application.interfaces import IYoloProcessProducer
from app.config import app_settings


@dataclass()
class YoloProcessProducer(IYoloProcessProducer):
    _rabbit_broker: RabbitBroker

    async def send(self, data: YoloProcessDto) -> None:
        await self._rabbit_broker.publish(
            msgspec.json.encode(data), queue=app_settings.yolo_queue
        )
