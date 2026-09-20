from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Exercise(Base):
    __tablename__ = "table_exercise"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    muscle_group: Mapped[str] = mapped_column(String(50), nullable=False)
    difficulty: Mapped[str] = mapped_column(String(50), nullable=False)
    equipment: Mapped[str|None] = mapped_column(String(100), nullable=True)
    instruction: Mapped[str|None] = mapped_column(String(50), nullable=True)
    