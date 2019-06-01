# 파일명과 클래스명이 달라야 더 잘됨.
# 파일명은 모듈이라고 정의하며, 모듈안에 클래스는 여러개 만들수 있다.
# 클래스는 private, public 등의 개념이 없고, 다 public임.
# 들여쓰기로 모든 것을 판단함.

class Calculator:
    # 초기화 : (java) 생성자 같은 느낌으로 이해 할 수 있을 것 같음.
    # self : self를 사용하여 자신의 클래스내 함수(메소드) 접근 / 반드시 존재해야함. == (java)this
    def __init__(self, first, second):
        self.first = first
        self.second = second

    #덧셈
    def sum(self):
        return self.first + self.second

    #뺄셈
    def sub(self):
        return self.first - self.second

    #곱하기
    def mul(self):
        return self.first * self.second

    #나누기
    def div(self):
        return self.first / self.second