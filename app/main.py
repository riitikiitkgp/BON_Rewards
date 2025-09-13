from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="BON Rewards API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Users
@app.post("/users/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

# Bills
@app.post("/bills/", response_model=schemas.BillOut)
def create_bill(bill: schemas.BillCreate, db: Session = Depends(get_db)):
    return crud.create_bill(db, bill)

# Pay Bill
@app.post("/bills/pay/", response_model=schemas.BillWithRewardOut)
def pay_bill(bill_pay: schemas.BillPay, db: Session = Depends(get_db)):
    result = crud.pay_bill(db, bill_pay)
    if not result:
        raise HTTPException(status_code=404, detail="Bill not found")
    bill, reward = result
    return schemas.BillWithRewardOut(
        bill_id=bill.bill_id,
        user_id=bill.user_id,
        due_date=bill.due_date,
        payment_date=bill.payment_date,
        reward=reward
    )

# Get Rewards
@app.get("/rewards/{user_id}", response_model=List[schemas.RewardOut])
def get_rewards(user_id: int, db: Session = Depends(get_db)):
    rewards = db.query(models.Reward).filter(models.Reward.user_id == user_id).all()
    return rewards
