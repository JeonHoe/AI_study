import os
import zipfile

def function1(sel, fpName):
    if not os.path.isfile(fpName):
        print("해당 파일명을 가진 파일이 없습니다.")
    if sel in ["해제", "압축"]:
        if sel == "압축":
            zipName = fpName.split(".")[0]
            zipName = zipName + ".zip"
            zipFp = zipfile.ZipFile(zipName,"w")
            zipFp.write(fpName)
            zipFp.close()
        else:
            clearName = fpName.split(".")[0]
            clearName = clearName + ".txt"
            clearFp = zipfile.ZipFile(fpName)
            clearFp.extract(clearName)



if __name__ == "__main__":
    sel = input("어떤 작업을 하시겠습니까(압축 또는 해제):")
    fpName = input("파일 이름을 입력하세요:")
    function1(sel, fpName)