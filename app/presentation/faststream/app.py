import msgspec
from dishka import make_container
from faststream import FastStream
from faststream.rabbit import RabbitBroker, RabbitMessage

from app.application.dto import YoloProcessDto
from app.application.services import YoloService
from app.config import app_settings
from app.ioc import ApplicationProvider, ImageProvider, InfrastructureProvider

container = make_container(
    InfrastructureProvider(), ApplicationProvider(), ImageProvider()
)

broker = container.get(RabbitBroker)

app = FastStream(broker)

yolo_service = container.get(YoloService)


@broker.subscriber(app_settings.yolo_queue)
async def base_handler(message: RabbitMessage) -> None:
    data = msgspec.json.decode(message.body, type=YoloProcessDto)

    await yolo_service.perform_yolo(yolo_id=data.yolo_id)
