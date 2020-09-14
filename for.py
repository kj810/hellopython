# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in range(1, 6): #[0,1,2,3,4]
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨","토르","그루트"]
# for customer in starbucks:
#     print("{0}손님, 커피가 준비되었습니다.".format(customer))



# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102 ,103  나도코딩 https://youtu.be/kWiCuklohdY?t=8351  한 줄 for 문
students = [1, 2, 3, 4, 5]
print(students)
students = [i+100 for i in students]
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man","Thor","i am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환 
students = ["Iron man","Thor","i am groot"]
students = [i.upper() for i in students]
print(students)