from fastapi import FastAPI
from data.db import Base, engine
from services.auth import auth

app = FastAPI()

# DB Init
Base.metadata.create_all(engine)

# Include routes
app.include_router(
    auth.router,
    prefix="/user",
    tags=["user"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}
