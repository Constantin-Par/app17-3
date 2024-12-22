from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from slugify import slugify

from schemas import CreateTask, UpdateTask
from models import *

router_task = APIRouter(prefix='/task', tags=['task'])


@router_task.get('/')
async def all_tasks():
    pass


@router_task.get('/task_id')
async def task_by_id():
    pass


@router_task.post('/create')
async def create_task():
    pass


@router_task.put('/update')
async def update_task():
    pass


@router_task.delete('/delete')
async def delete_task():
    pass
