# import theather_module
# theather_module.price(3) # 3명이서 영화보러갔을 때 가격
# theather_module.price_morning(4) 
# theather_module.price_soldier(5)

# import theather_module as tm # 모듈명을 줄여서 짧게 사용
# tm.price(3)
# tm.price_morning(3)
# tm.price_soldier(3)

# from theather_module import *
# # from random import * 

# price(3)
# price_morning(3)
# price_soldier(3)

from theather_module import price, price_morning# 어떤 함수만 사용할지 선택
price(5)
price_morning(3)
# price_soldier(2)

from theather_module import price_soldier as price
price(1)