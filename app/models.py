from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    bills = relationship("Bill", back_populates="user")
    rewards = relationship("Reward", back_populates="user")

class Bill(Base):
    __tablename__ = "bills"
    bill_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    due_date = Column(Date, nullable=False)
    payment_date = Column(Date, nullable=True)

    user = relationship("User", back_populates="bills")

class Reward(Base):
    __tablename__ = "rewards"
    reward_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    reward_name = Column(String, nullable=False)

    user = relationship("User", back_populates="rewards")
