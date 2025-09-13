from pydantic import BaseModel
from datetime import date
from typing import Optional, List

# User
class UserCreate(BaseModel):
    name: str
    email: str

class UserOut(BaseModel):
    user_id: int
    name: str
    email: str

    class Config:
        orm_mode = True

# Bill
class BillCreate(BaseModel):
    user_id: int
    due_date: date

class BillPay(BaseModel):
    bill_id: int
    payment_date: date

class BillOut(BaseModel):
    bill_id: int
    user_id: int
    due_date: date
    payment_date: Optional[date]

    class Config:
        orm_mode = True

# Reward
class RewardOut(BaseModel):
    reward_id: int
    user_id: int
    reward_name: str

    class Config:
        orm_mode = True

# Combined response for bill payment
class BillWithRewardOut(BillOut):
    reward: Optional[RewardOut] = None
