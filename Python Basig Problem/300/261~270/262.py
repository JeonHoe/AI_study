class Stock:
    def __init__(self, name, code):
        self.name = name
        self.code = code


if __name__ == '__main__':
    samsung = Stock("삼성전자", "005930")
    print(samsung.name)
    print(samsung.code)