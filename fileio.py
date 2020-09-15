# #파일 입출력

# score_file = open("score.txt", "w", encoding="utf8") #이 파일은 쓰기용도 (덮어쓰기가 됨)
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") #덮어쓰기가 아니라 추가하기
# score_file.write("과학 : 80\n")
# score_file.write("코딩 : 100")

# # 출력하기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# # 한 줄씩 출력
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄 별로 읽기 , 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 파일이 몇 줄인지 모를때
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#   line = score_file.readline()
#   if not line:
#     break
#   print(line, end="")
# score_file.close()


# 리스트에 값을 넣어 처리
# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines:
#   print(line, end="")

# score_file.close()