from fastapi import APIRouter
from repository import TaskRepository
from schemas import STaskAdd, STask, STaskId

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks

@router.post("")
async def add_task(task: STaskAdd) -> STaskId:
   task_id = await TaskRepository.add_one(task)
   return {"ok": True, "task_id": task_id}