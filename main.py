from fastapi import FastAPI
from database import create_tables, delete_tables
from contextlib import asynccontextmanager


from router import router as tasks_router

# changes

@asynccontextmanager
async def lifespan(app:FastAPI):
    await delete_tables()
    print("Database cleanup")
    await create_tables()
    print("Database is ready for use")
    yield
    print("Shut down")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)
