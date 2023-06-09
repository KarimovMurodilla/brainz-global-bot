from sqlalchemy.orm import relationship

from sqlalchemy import (
    Column, BigInteger, 
    String, Integer, ForeignKey)

from utils.db_api.base import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(50))
    talent = relationship("Talent", back_populates="User")
    recruiter = relationship("Recruiter", back_populates="User")



class Talent(Base):
    __tablename__ = "talent"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    fullname = Column(String(50))
    role = Column(String(10), default="Талант")
    user_id = Column(Integer, ForeignKey("user.user_id"))
    user = relationship("User", back_populates="talent")


class Recruiter(Base):
    __tablename__ = "recruiter"

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    fullname = Column(String(50))
    role = Column(String(10), default="Рекрутер")
    company = Column(String(150))
    user_id = Column(Integer, ForeignKey("user.user_id"))
    user = relationship("User", back_populates="talent")