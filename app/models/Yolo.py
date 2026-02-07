import enum

from sqlalchemy import String
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import BaseModel


class ProcessingState(enum.StrEnum):
    PENDING = "PENDING"
    FINISHED = "FINISHED"


class YoloModel(BaseModel):
    __tablename__ = "yolo"

    camera_data: Mapped[dict] = mapped_column(JSONB(), default={})

    yolo_result: Mapped[dict] = mapped_column(JSONB(), default={})

    state: Mapped[ProcessingState] = mapped_column(String())

    result: Mapped[str] = mapped_column(default="Дождитесь завершения проверки.")
