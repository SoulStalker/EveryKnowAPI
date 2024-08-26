from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, MetaData, Table, Text, func, JSON, Boolean

metadata = MetaData()

category = Table(
    'category',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False, unique=True),
    Column('parent_id', Integer, ForeignKey('category.id')),
    Column('department_id', Integer, ForeignKey('department.id')),
)


article = Table(
    'article',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(30), nullable=False, unique=True),
    Column('content', Text, nullable=False),
    Column('created_at', DateTime, nullable=False, server_default=func.now()),
    Column('updated_at', DateTime, nullable=False, server_default=func.now(), onupdate=func.now()),
    Column('author_id', Integer, ForeignKey('user.id')),
    Column('category_id', Integer, ForeignKey('category.id')),
)


role = Table(
    'role',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False, unique=True),
    Column('permission', JSON, nullable=False),
)

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(30), nullable=False),
    Column('last_name', String(30), nullable=False),
    Column('email', String(50), nullable=False, unique=True),
    Column('hashed_password', String(50), nullable=False),
    Column('tg_id', String(50), nullable=False, unique=True),
    Column('register_date', DateTime, nullable=False, server_default=func.now()),
    Column('department_id', Integer, ForeignKey('department.id')),
    Column('role_id', Integer, ForeignKey('role.id')),
    Column('is_active', Boolean, nullable=False, default=True),
    Column('is_superuser', Boolean, nullable=False, default=False),
    Column('verified', Boolean, nullable=False, default=False),
)


department = Table(
    'department',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False, unique=True),
)


tag = Table(
    'tag',
    metadata,
    Column('tag_id', Integer, primary_key=True),
    Column('tag_name', String(30), nullable=False, unique=True),
)
