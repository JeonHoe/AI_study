import os
from cryptography.fernet import Fernet as frnt

        

if __name__ == "__main__":
    order = input("어떤 작업을 하시겠습니까(enc 또는 dec):")
    fpName = input("파일 이름을 입력하세요:")

    
    if not os.path.isfile(fpName):
        print("해당 파일명을 가진 파일이 없습니다.")
    if order in ["enc", "dec"]:
        key = b'LPg0dqj9L-EFbXyaVzEllb8oEe4piRrqKYxmtSRiw4Y='
        cipher_suite = frnt(key)
        str_list = []
        if order == "enc":
            with open(fpName, 'r') as fp:
                while True:
                    line = fp.readline()
                    if not line:
                        break
                    line = line.rstrip("\n")
                    secret_str = cipher_suite.encrypt(bytes(line, "UTF-8"))
                    str_list.append(secret_str)
        
            enc_fpName = fpName.split(".")[0] + ".bin"
        
            with open(enc_fpName, "wb") as encFp:
                for enc_line in str_list:
                    encFp.write(enc_line)

        if order == "dec":
            with open(fpName, 'rb') as fp:
                line = fp.read()
                dec_str = cipher_suite.decrypt(line)
                str_list.append(dec_str)
        
            dec_fpName = fpName.split(".")[0] + ".txt"
        
            with open(dec_fpName, "w") as decFp:
                for dec_line in str_list:
                    dec_line = str(dec_line)
                    dec_line = dec_line[2:-1]
                    dec_line += "\n"
                    decFp.writelines(dec_line)