from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings
from .todo.routes import router as todo_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")

def read_root():
  return {"Hello": "World"}

app.include_router(todo_router, tags=["tasks"], prefix="/task")

@app.on_event("startup")
async def startup_db():
  app.mongodb_client = AsyncIOMotorClient(settings.DB_URL)
  app.mongodb = app.mongodb_client[settings.DB_NAME]
  
@app.on_event("shutdown")
async def shutdown_db():
  app.mongodb_client.close()