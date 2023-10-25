#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage

print(storage.all())
print("load data")


a = BaseModel()
a.save()
