from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.auth import create_access_token, get_current_user
from app.security import hash_password, verify_password
from app.database import Base, engine, get_db
from app import models, schemas
from fastapi.security import OAuth2PasswordRequestForm
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

@app.post("/login", response_model=schemas.Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    db_user = (
    db.query(models.User)
    .filter(models.User.email == form_data.username)
    .first()
)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    if not verify_password(form_data.password, db_user.password):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }
@app.get("/me")
def get_me(
    current_user: models.User = Depends(get_current_user)
):
    return current_user

@app.post("/expenses", response_model=schemas.ExpenseResponse)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        owner_id=current_user.id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense
@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
def get_expenses(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    expenses = (
        db.query(models.Expense)
        .filter(models.Expense.owner_id == current_user.id)
        .all()
    )

    return expenses

@app.put("/expenses/{expense_id}", response_model=schemas.ExpenseResponse)
def update_expense(
    expense_id: int,
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_expense = (
        db.query(models.Expense)
        .filter(
            models.Expense.id == expense_id,
            models.Expense.owner_id == current_user.id
        )
        .first()
    )

    if not db_expense:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    db_expense.title = expense.title
    db_expense.amount = expense.amount
    db_expense.category = expense.category

    db.commit()
    db.refresh(db_expense)

    return db_expense

@app.delete("/expenses/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    expense = (
        db.query(models.Expense)
        .filter(
            models.Expense.id == expense_id,
            models.Expense.owner_id == current_user.id
        )
        .first()
    )

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}
