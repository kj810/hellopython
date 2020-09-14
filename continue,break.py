absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("{0} 번은 끝나고 교무실로 따라와".format(student))
        continue
    print("{0}, 책을 읽어봐.".format(student))
print("오늘 수업 여기까지..")


