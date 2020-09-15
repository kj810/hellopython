# keyword parameter

# def profile(name, age, main_lang):
#   print(name, age, main_lang)


# profile(name="유재석", main_lang="파이썬", age=20)
# profile(name="김태호", age=22,main_lang="자바" )


# # Variable parameter (*language)

# # def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# def profile(name, age, *language):
#   print("이름 : {0}\t나이 : {1}\t".format(name, age),end=" ")
#   # print(lang1, lang2, lang3, lang4, lang5)
#   for lang in language:
#     print(lang, end=" ")
#   print()
# profile("유재석", 20, "Python","java","C","C++","C#")
# profile("김태호", 25, "Kotlin","Swift", "", "", "")


# 지역변수(함수 내에서만 쓸 수 있는 것. 함수가 호출되었을때 만들어지고 끝나면 끝) 
# 전역변수(프로그램 어디에서든 불러올 수 있는 것)

gun = 10 # 전역 변수

def checkpoint(soldiers): #경계근무
  # gun = 20 지역 변수.
  global gun # 전역 공간에 있는 gun을 사용하겠다는 표시.
  gun = gun - soldiers
  print("[함수 내] 남은 총 = {0}".format(gun))

def checkpoint_ret(gun, soldiers):
  gun = gun - soldiers
  print("[함수 내] 남은 총 = {0}".format(gun))
  return gun # 변경 된 값을 전역 공간에 반영함


print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
