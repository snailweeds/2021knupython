# 해달이의 집에서 학교까지의 거리
# 숫자 두개를 입력받아 둘 중 큰 값에서 작은 값을 빼서 거리 구하기

input1 = input("첫 번째 수를 입력하시오.")
input2 = input("두 번째 수를 입력하시오.")

if(input1>input2):
    result = int(input1)-int(input2)
elif(input1==input2):
    result = 0
else:
    result = int(input2)-int(input1)

print(result, "km")
