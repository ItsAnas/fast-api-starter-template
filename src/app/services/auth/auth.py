from fastapi import APIRouter
from data.db import session
from fastapi import status, HTTPException
from pydantic import BaseModel
from models.user import User
from services.auth.schema import UserCreate, UserGet
from sqlalchemy import or_

router = APIRouter()


@router.post("/")
async def create_user(user_in: UserCreate):
    """
    Create a user in the database
    """
    user = (
        session.query(User)
        .filter(or_(User.email == user_in.email, User.username == user_in.username))
        .first()
    )

    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in the system.",
        )

    user = User(
        username=user.username,
        email=user.email,
        hashed_password=user.password,  # TODO: Need to hash
        is_active=True,  # TODO: Email confirmation
        is_superuser=False,  # TODO: Email confirmation
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    return user


@router.get("/{user_id}")
async def create_user(user_id):
    """
    Get information about the current user
    """
    user = session.query(User).get(user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="This user does not exist.",
        )
    return user