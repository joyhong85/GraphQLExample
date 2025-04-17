from typing import List

import strawberry
from strawberry_django.optimizer import DjangoOptimizerExtension

from api.resolvers import get_student, get_lecture
from api.types import Student, Lecture


@strawberry.type
class Query:
    @strawberry.field
    def get_student(self, id: str) -> List[Student]:
        # print(id)
        # return [Student(name="a", identifier="1", grade="2")]
        return get_student(id)

    @strawberry.field
    def get_lecture(self, name: str) -> List[Lecture]:
        return get_lecture(name)

schema = strawberry.Schema(
    query=Query,
    extensions=[DjangoOptimizerExtension, ],
)