from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, MetaData, Table, Text, func, JSON

metadata = MetaData()

categories = Table(
    'categories',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False, unique=True),
    Column('parent_id', Integer, ForeignKey('categories.id')),
)


articles = Table(
    'articles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(30), nullable=False, unique=True),
    Column('content', Text, nullable=False),
    Column('created_at', DateTime, nullable=False, server_default=func.now()),
    Column('updated_at', DateTime, nullable=False, server_default=func.now(), onupdate=func.now()),
    Column('author_id', Integer, ForeignKey('users.id')),
    Column('category_id', Integer, ForeignKey('categories.id')),
)


roles = Table(
    'roles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False, unique=True),
    Column('permission', JSON, nullable=False),
)

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String(30), nullable=False),
    Column('last_name', String(30), nullable=False),
    Column('email', String(50), nullable=False, unique=True),
    Column('password', String(50), nullable=False),
    Column('tg_id', String(50), nullable=False, unique=True),
    Column('register_date', DateTime, nullable=False, server_default=func.now()),
    Column('department_id', Integer, ForeignKey('departments.id')),
    Column('role_id', Integer, ForeignKey('roles.id')),
)

departments = Table(
    'departments',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30), nullable=False, unique=True),
)


tags = Table(
    'tags',
    metadata,
    Column('tag_id', Integer, primary_key=True),
    Column('tag_name', String(30), nullable=False, unique=True),
)
