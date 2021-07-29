def people_num(*args):
    print("공부하는 학생 수는?: ", end="")
    print(args)
    result = len(args)
    return result

value = people_num("해달이", "사스미", "시라용", "부기", "매기")
print(value, "멍")