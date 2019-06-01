# 패키지와 모듈, 생성한 클래스 불러오기.
from calculator.model import Calculator as Calc

# 메인 메소드로 이해 가능.
# public static void main(String[] args){}
if __name__ == '__main__':
    # a = int(input('첫번째 수')) # input값은 무조건 문자값으로 받으므로 int형으로 변환해줘야 함.
    # b = int(input('두번째 수'))
    # calc = Calc(a, b)

    calc = Calc(int(input('첫번째 수')), int(input('두번째 수'))) # input은 (java)scanner의 역할을 함. 콘솔로 입력 받을 수 있음.
    print('{} + {} = {}'.format(calc.first, calc.second, calc.sum())) # (java)출력서식 printf의 역할을 함.
