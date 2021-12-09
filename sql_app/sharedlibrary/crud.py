from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_users(db: Session):
    return db.query(models.User).all()

def create_user(db:Session, request):
    new_user = request
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

