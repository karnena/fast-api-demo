from typing import List
from fastapi import Depends, FastAPI, HTTPException
from passlib.context import CryptContext

from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import mode
from starlette.responses import Response
from sharedlibrary import crud,models, schemas

from sharedlibrary.database import SessionLocal, engine
from sharedlibrary.models import ProjectUser

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

pwt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

     
@app.post('/user')
def create(request: schemas.UserData, db: Session = Depends(get_db)):
    new_user = models.User(name=request.name) 
    db.add(new_user)
    db.commit() 
    db.refresh(new_user)
    return "success"

@app.post('/project')
def create(request: schemas.ProjectData, db: Session = Depends(get_db)):
    new_project = models.Project(name = request.name)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return "ok"

@app.post('/user/project/{projectId}')
def create(projectId,request: schemas.UserId, db: Session = Depends(get_db)):
    new_project = models.ProjectUser(user_id= request.user_id, project_id = projectId )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return "done"

@app.get('/user/project/{projectId}')
def showProject(projectId :int, db:Session = Depends(get_db)):
    project = db.query(models.User).select_from(models.ProjectUser).join(models.User, models.User.id == models.ProjectUser.user_id).join(models.Project, models.Project.id == models.ProjectUser.project_id).filter(models.Project.id == projectId).all()
    # project = db.query(models.Project).filter(models.Project.id == projectId).first()
    if not project:
        raise HTTPException(status_code=404, details = "project with id {projectId} notfound")
    return project
 
@app.get('/user/project/')
def showProject(db:Session = Depends(get_db)):
    project = db.query(models.User).select_from(models.ProjectUser).join(models.User, models.User.id == models.ProjectUser.user_id).join(models.Project, models.Project.id == models.ProjectUser.project_id).filter(models.Project.id ==1).all()
    return project

# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
# @app.post('/signup/')
# def create_user(request: schemas.User, db: Session = Depends(get_db)):
#     crud.create_user(db, request)
#     return "done"



# @app.get("/login")
# def read_item(user_name:str, password:str,db: Session = Depends(get_db)):
#     users = crud.get_users(db)
#     us = ''
#     ps= ''
#     for i in users:
#         if(i.user_name == user_name):
#             us = i.user_name
#             ps = i.password
#     if user_name == us:
#         if str(ps) == password:
#             payload_data = {"user_name": user_name}
#             encoded_jwt = jwt.encode(payload=payload_data, key="secreat")
#             s['auth'].append(encoded_jwt)
#             return("login success", encoded_jwt)
#         else:
#             return("username and password not matched")

#     else:
#         return("login error")



# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship, Session

# # Make the engine
# engine = create_engine("sqlite:///./sql_app.db", future=True, echo=False)

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