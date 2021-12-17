from typing import Text
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TEXT

from sharedlibrary.database import Base


# class User(Base):
#     __tablename__ = "user_detail"

#     id = Column(Integer, primary_key=True, index=True)
#     user_name = Column(TEXT, unique=True)
#     email = Column(TEXT, unique=True)
#     password = Column(TEXT)

class ProjectUser(Base): 
    __tablename__ = "project_users"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    project_id = Column(Integer, ForeignKey('projects.id')) 
    user = relationship("User", back_populates="projects")
    project = relationship("Project", back_populates="users")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    projects = relationship('ProjectUser', back_populates='user')
class Project(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    users = relationship('ProjectUser', back_populates='project')



# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship, Session

# # Make the engine
# engine = create_engine("sqlite+pysqlite:///:memory:", future=True, echo=False)

# # Make the DeclarativeMeta
# Base = declarative_base()


# class User(Base):
#     _tablename_ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     projects = relationship('Project', secondary='project_users', back_populates='users')


# class Project(Base):
#     _tablename_ = "projects"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     users = relationship('User', secondary='project_users', back_populates='projects')


# class ProjectUser(Base):
#     _tablename_ = "project_users"

#     id = Column(Integer, primary_key=True)
#     notes = Column(String, nullable=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     project_id = Column(Integer, ForeignKey('projects.id'))



# # Create the tables in the database
# Base.metadata.create_all(engine)

# # Test it
# with Session(bind=engine) as session:

#     # add users
#     usr1 = User(name="bob")
#     session.add(usr1)

#     usr2 = User(name="alice")
#     session.add(usr2)

#     session.commit()

#     # add projects
#     prj1 = Project(name="Project 1")
#     session.add(prj1)

#     prj2 = Project(name="Project 2")
#     session.add(prj2)

#     session.commit()

#     # map users to projects
#     prj1.users = [usr1, usr2]
#     prj2.users = [usr2]

#     session.commit()


# with Session(bind=engine) as session:

#     print(session.query(User).where(User.id == 1).one().projects)
#     print(session.query(Project).where(Project.id == 1).one().users)