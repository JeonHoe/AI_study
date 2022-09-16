class Parent:
    def call(self):
        print('부모 호출')
    
class Child(Parent):
    def call(self):
        print('자식 호출')

me = Child()
me.call()