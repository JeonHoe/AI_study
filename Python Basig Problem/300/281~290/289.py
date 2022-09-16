class Parent:
    def __init__(self):
        print("부모 생성")

    def call(self):
        print('부모 호출')
    
class Child(Parent):
    def __init__(self):
        print("자식 생성")

    def call(self):
        print('자식 호출')

me = Child()
