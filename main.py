from fastapi import FastAPI
from routers.task import router_task
from routers.user import router_user

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(router_task)
app.include_router(router_user)

# pip install alembic
# pip install uvicorn
# pip install fastapi
# pip install python-slugify

# uvicorn main:app
# alembic init migrations
# alembic revision
# alembic revision --autogenerate -m "Initial migration"
# alembic upgrade head