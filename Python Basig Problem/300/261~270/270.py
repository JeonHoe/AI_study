class Stock:
    def __init__(self, name, code, PER, PBR, res):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.res = res

    def set_name(self, name):
        self.name = name

    def set_code(self, code):
        self.code = code

    def set_per(self, PER):
        self.PER = PER

    def set_pbr(self, PBR):
        self.PBR = PBR

    def set_dividend(self, res):
        self.res = res

    def get_name(self):
        return self.name
    
    def get_code(self):
        return self.code


if __name__ == '__main__':
    a = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
    b = Stock("현대차", "005380", 8.70, 0.35, 4.27)
    c = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
    list1 = [a, b, c]
    for i in list1:
        if type(i) == Stock:
            print("코드 :",i.code,"PER :", i.PER)