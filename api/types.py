from typing import List, Optional

import strawberry_django
from strawberry import auto

from api import models


@strawberry_django.type(models.Student)
class Student:
    name: auto
    identifier: auto
    grade: auto
    course: List["Lecture"]


@strawberry_django.type(models.Lecture)
class Lecture:
    name: auto
    classroom: auto
    professor: "Professor"

@strawberry_django.type(models.Professor)
class Professor:
    name: auto
    identifier: auto
    phone: auto

