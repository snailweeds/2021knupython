f = open("haedal_for.txt", "w")

for i in range(100):
    f.write(f"Hello Haedal! {i}\n")

print("쓰기 종료")
f.close()