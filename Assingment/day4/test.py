# def invest():
#  yield 1
#  yield 2
#  yield 3
#  yield 4
#  yield 5
# res = invest()
# print(res)
# print(list(res))
#  next(res) # 1
#  next(res) # 2
#  next(res) # 3
#  next(res) # 4
#  next(res) # 5
#  next(res) # StopIteration
# def alert(fnref):
#  def wrapper(*args,**kwargs):
#     print("before")
#     res = fnref(*args,**kwargs)
#     print("after")
#     return res
#  return wrapper

# @alert
# def withdraw():
#   pass
# @alert
# def deposit():
#   pass
# @alert
# def transfer():
#   pass
# def checkbalance():
#   pass

# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.title("TITLE OF CHART")
# plt.xlabel("label1")
# plt.ylabel("label2")

# plt.plot(xpoints, ypoints)
# plt.show()

