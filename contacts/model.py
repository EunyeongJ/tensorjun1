"""
name, phone, email, addr를 파라미터로 전달받음
"""
class Contact:
    # init
    def __init__(self, name, phone, email, addr):
        self.name = name
        self.phone = phone
        self.email = email
        self.addr = addr

    # print
    def print_info(self):
        print('이름은 \'{}\', 전화번호는 \'{}\', 이메일은 \'{}\', 주소는 \'{}\' 입니다.'.format(self.name, self.phone, self.email, self.addr))

    # setter
    @staticmethod
    def set_contact():
        name = input('이름 : ')
        phone = input('전화번호 : ')
        email = input('이메일 : ')
        addr = input('주소 : ')
        contact = Contact(name, phone, email, addr) # 초기화 호출
        return contact

    # getter
    # class 내의 모든 method의 파라미터는 self가 있어야 하는데, 집합체를 파라미터로 사용하는 경우 @staticmethod를 붙여준다.
    @staticmethod
    def get_contacts(list):
        for i in list:
            i.print_info()

    # 연락처 삭제
    @staticmethod
    def del_contact(list, name):
        for i, t in enumerate(list): # enumerate는 list내를 한번만 돌아라. 그리고 변수 t로 받음. i는 인덱스이고, t는 변수로 보임.
            if t.name == name:
                del list[i]

    # 메뉴 선택
    @staticmethod
    def print_menu():
        print('---------------------')
        print('1. 연락처 입력')
        print('2. 연락처 출력')
        print('3. 연락처 삭제')
        print('4. 종료 ')
        print('---------------------')
        menu = input('메뉴를 선택해주세요 : ')
        return int(menu)


    @staticmethod
    def run():
        list = []
        while 1 :
            menu = Contact.print_menu()
            if menu == 1:
                t = Contact.set_contact()
                list.append(t)
            elif menu == 2:
                t = Contact.get_contacts(list)
            elif menu == 3:
                name = input('삭제할 이름 : ')
                Contact.del_contact(list, name)
            elif menu == 4:
                break
