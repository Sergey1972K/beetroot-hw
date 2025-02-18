# homework
"""The complexity of the algorithms of the following functions"""


# Складність O(n * m), де n - довжина first_list, m - довжина second_list
def question1(first_list: list[int], second_list: list[int]) -> list[int]:
    res: list[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

# Складність O(1), оскільки цикл виконується сталу кількість разів (10)
def question2(n: int) -> int:
	for _ in range(10):
		n **= 3
	return n

# Складність O(n * m), де n - довжина first_list, m - довжина second_list
def question3(first_list: list[int], second_list: list[int])-> list[int]:
   temp: list[int] = first_list[:]
   for el_second_list in second_list:
      flag = False
      for check in temp:
         if el_second_list == check:
            flag = True
            break
      if not flag:
         temp.append(second_list)
   return temp

# Складність O(n), де n - довжина input_list
def question4(input_list: list[int]) -> int:
  res: int = 0
  for el in input_list:
    if el > res:
      res = el
  return res

# Складність O(n^2), оскільки  два вкладені цикли, кожен з яких проходить n ітерацій
def question5(n: int) -> list[tuple[int, int]]:
    res: list[tuple[int, int]] = []
    for i in range(n):
        for j in range(n):
            res.append((i, j))
    return res

# Складність O(log n), оскільки значення n ділиться на 2 в кожній ітерації циклу
def question6(n: int) -> int:
    while n > 1:
        n /= 2
    return n
