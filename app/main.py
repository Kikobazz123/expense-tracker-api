from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app import models, schemas
from app.security import hash_password

app = FastAPI(title="Expense Tracker API")

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Expense Tracker API is running!"}


@app.post("/register", response_model=schemas.UserResponse)
def register_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user