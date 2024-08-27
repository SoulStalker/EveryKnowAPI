
from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    first_name: str
    last_name: str
    tg_id: str
    role_id: int
    department_id: int


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    tg_id: str
    role_id: int
    department_id: int


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
    tg_id: str
    role_id: int
    department_id: int