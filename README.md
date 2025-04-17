# 데모용
- https://strawberry.rocks/docs/django 를 활용하여 GraphQL 서버를 생성하는 데모용으로 작성한 내용임

# 파이썬 버전
- Python 3.8 사용

# 예제 쿼리
~~~
{
  getStudent(id:"a"){
    name
    identifier
    grade
    course{
      name
      classroom
    }
  }
}
~~~
~~~
query GetLecture($name: String!) {
  getLecture(name:$name){
    name
    classroom
  }
}
# variable
{
  "name":"국어"
}
~~~
~~~
{
  getStudent(id:"a"){
    name
    identifier
    grade
    course{
      name
      classroom
      professor{
        name
      }
    }
  }
}
~~~
