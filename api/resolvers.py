from typing import List

from api.types import Student, Lecture, Professor


def get_student(id: str) -> List[Student]:
    return [Student(name="a", identifier="1", grade="2", course=get_lecture(id))]


def get_lecture(id: str) -> List[Lecture]:
    sample_dict = {"a":[("국어","바른생활관"),("수학","정석관")], "b":[("수학","정석관")]}
    return [Lecture(name=x[0], classroom=x[1], professor=get_professor(x[0])) for x in sample_dict[id]]


def get_professor(id: str) -> List[Professor]:
    sample_dict = {"국어":"홍길동", "영어":"해밍턴", "수학":"방정식"}
    return Professor(name=sample_dict[id], identifier="PROF1", phone="112233")