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
