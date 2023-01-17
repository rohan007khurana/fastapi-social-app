from fastapi import FastAPI
from .database import engine
from . import models
from .routers import posts, users, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# Below command is used to generate table using sqlalchemy but now we are using alembic
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}