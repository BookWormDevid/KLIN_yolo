from dataclasses import dataclass
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.application.interfaces import IYoloRepository
from app.models.Yolo import YoloModel


@dataclass
class YoloRepository(IYoloRepository):
    session: async_sessionmaker[AsyncSession]

    async def get_by_id(self, yolo_id: UUID) -> YoloModel:
        async with self.session() as session:
            query = select(YoloModel).where(YoloModel.id == yolo_id).limit(1)
            imference = await session.scalar(query)
            if not imference:
                raise ValueError
            return imference

    async def create(self, model: YoloModel) -> YoloModel:
        async with self.session() as session:
            async with session.begin():
                session.add(model)
            await session.refresh(model)
            return model

    async def update(self, model: YoloModel) -> None:
        async with self.session() as session:
            async with session.begin():
                await session.merge(model)
            await session.commit()
