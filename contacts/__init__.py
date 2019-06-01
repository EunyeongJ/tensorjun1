from contacts.model import Contact

if __name__ == '__main__':
    # 클래스의 __init__ 함수를 먼저 거쳐서 초기화 한 후 실행
    """
    name = input('이름 : ')
    phone = input('전화번호 : ')
    email = input('이메일 : ')
    addr = input('주소 : ')
    Con(name, phone, email, addr) # contact 하나만 사용. scalar
    """

    # 인공지능에서 input 값을 많이 줄수록 정확한 값이 도출됨. vector
    # 인공지능에서 원하는 값은 하나만 나와야 함. scalar

    Contact.run()