from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

def create_user(db: Session, user: schemas.UserCreate):
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        return existing_user  # or raise an exception if you want
    db_user = models.User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_bill(db: Session, bill: schemas.BillCreate):
    db_bill = models.Bill(user_id=bill.user_id, due_date=bill.due_date)
    db.add(db_bill)
    db.commit()
    db.refresh(db_bill)
    return db_bill

def pay_bill(db: Session, bill_pay: schemas.BillPay):
    bill = db.query(models.Bill).filter(models.Bill.bill_id == bill_pay.bill_id).first()
    if not bill:
        return None

    bill.payment_date = bill_pay.payment_date
    db.commit()
    db.refresh(bill)

    # Check last 3 bills for reward eligibility
    bills = db.query(models.Bill)\
        .filter(models.Bill.user_id == bill.user_id)\
        .order_by(models.Bill.due_date.desc())\
        .limit(3).all()

    reward = None
    if len(bills) == 3 and all(b.payment_date and b.payment_date <= b.due_date for b in bills):
        reward_name = "$10 Amazon Gift Card"
        reward = models.Reward(user_id=bill.user_id, reward_name=reward_name)
        db.add(reward)
        db.commit()
        db.refresh(reward)

    return bill, reward
