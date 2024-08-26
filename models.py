from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
import datetime


class Script(Base):
    __tablename__ = "scripts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    path = Column(String(255))
    venv_path = Column(String(255))
    schedule = Column(String(100))
    active = Column(Boolean, default=True)
    logs = relationship("Log", back_populates="script")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "path": self.path,
            "venv_path": self.venv_path,
            "schedule": self.schedule,
            "active": self.active,
        }


class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True)
    script_id = Column(Integer, ForeignKey("scripts.id"))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(20))
    message = Column(String(255))
    script = relationship("Script", back_populates="logs")

    def to_dict(self):
        return {
            "id": self.id,
            "script_id": self.script_id,
            "script_name": self.script.name if self.script else "Unknown",
            "timestamp": self.timestamp.isoformat(),
            "status": self.status,
            "message": self.message,
        }
