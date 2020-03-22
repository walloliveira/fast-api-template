from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.domains.models import User
from database import get_db

api = FastAPI()


class UserResponse(BaseModel):
    id: str
    email: str

    @classmethod
    def from_domain(cls, user: User):
        return UserResponse(
            id=user.id,
            email=user.email,
        )


@api.get('/users', response_model=UserResponse)
async def get(
        db: Session = Depends(get_db),
):
    first = db.query(User).first()
    return UserResponse.from_domain(first)


@api.post('/users', response_model=UserResponse)
async def post(
        db: Session = Depends(get_db),
):
    first = db.query(User).first()
    return UserResponse.from_domain(first)
