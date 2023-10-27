#!/usr/bin/python3

from models.base_model import BaseModel
from models import storage




a = BaseModel()
a.save()

print(storage.all())
print("load data")
