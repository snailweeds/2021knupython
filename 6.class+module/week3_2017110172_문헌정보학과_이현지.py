cur_tem = 20

def set_tem(des_tem):
    """
    온도를 설정하는 함수
    set_tem(설정할 온도)
    """
    if int(des_tem)>int(cur_tem):
        for i in range((int(des_tem)-int(cur_tem))+1):
            result = int(cur_tem) + i
            print(f"현재 온도는 {result}도 입니다.")
    elif int(des_tem)<int(cur_tem):
        for i in range((int(cur_tem)-int(des_tem))+1):
            result = int(cur_tem) - i
            print(f"현재 온도는 {result}도 입니다.")
    else:
        print(f"현재 온도는 {cur_tem}도 입니다.")
    
print("에어컨을 작동합니다.")

while True:
    a = input("원하는 온도를 설정해주세요: ")
    if a == "종료":
        print("에어컨을 종료합니다.")
        break
    elif int(a)>=18 and int(a)<=30:
        tem = set_tem(a)
        cur_tem = a
        continue
    else:
        print("입력을 확인해 주세요.")
        continue
