from fastapi import FastAPI
from sqladmin import Admin, ModelView

from utils.db_api.models import (
    User, School, 
    College, Texnikum, Lyceum
    )

from loader import db

engine = db.get_engine()

app = FastAPI()
admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    column_list = [User.user_id, User.username, User.first_name, User.last_name]


class SchoolAdmin(ModelView, model=School):
    column_list = [
        School.id, School.malumot, School.rahbariyat, 
        School.yonalish, School.qabul, School.savollar, School.boglanish
    ]

   
class CollegeAdmin(ModelView, model=College):
    column_list = [
        College.id, College.malumot, College.rahbariyat, 
        College.yonalish, College.qabul, College.savollar, College.boglanish
    ]

   
class TexnikumAdmin(ModelView, model=Texnikum):
    column_list = [
        Texnikum.id, Texnikum.malumot, Texnikum.rahbariyat, 
        Texnikum.yonalish, Texnikum.qabul, Texnikum.savollar, Texnikum.boglanish
    ]


class LyceumAdmin(ModelView, model=Lyceum):
    column_list = [
        Lyceum.id, Lyceum.malumot, Lyceum.rahbariyat, 
        Lyceum.yonalish, Lyceum.qabul, Lyceum.savollar, Lyceum.boglanish
    ]

   

admin.add_view(UserAdmin)
admin.add_view(SchoolAdmin)
admin.add_view(CollegeAdmin)
admin.add_view(TexnikumAdmin)
admin.add_view(LyceumAdmin)