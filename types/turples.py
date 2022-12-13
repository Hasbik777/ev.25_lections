# tuple() - кортеж, неизменяемый тип данных

# thistuples = 'apple', 'banna', 'cherry'
# print(thistuples)
# print(type(thistuples))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# print('List:', a.__sizeof__())
# print('Tuple:', b.__sizeof__())


# tuple_ = (1, 'h', 3)
# tuple_[1] = 2
# print(tuple_)

# print(dir(tuple))

# a = 1
# b = 2
# c = 3
# res = (a, b, c)
# print(res)
# new1, new2, new3 = res
# print(new1)
# print(new2)
# print(new3)

# a = (1, 2, 3)
# a = list(a)
# a.append(4)
# a = tuple(a)
# print(a)

# tuple_ = (1, 2, 3, 4, 5, 6, 7, 8, 5, 5)
# print(tuple_.count(5))
# print(tuple_.index(7))

# # -------------------------------------------------
# inputs 1:
# tuple_ = (1, 8, 3, 4, 5, 6, 8, 8, 9, 2)
# target = 8
# output:
# result = (8, 3, 5, 6, 8)

# inputs 2:
# tuple_ = (1, 2, 3, 8, 5, 1, 2)
# target = 8
# output:
# result = (8, 5, 1, 2)

# tuple_ = (1, 2, 3, 8, 5, 1, 2)
# target = 8
# if tuple_.count(target) > 1:
#     first = tuple_.index(target)
#     second = tuple_.index(target, first+1)
#     result = tuple_[first:second + 1]
# else:
#     first = tuple_.index(target)
#     result = tuple_[first: ]
# print(result)

# + *
# a = (1, 2, 3)
# b = (4, 5, 6)
# res = a + b
# print(res)

# a = (1, 2, 3)
# res = a * 3
# print(res)

# students = (
#     ('Елена', '13', 9, 'Москва'),
#     ('Ольга', '11', 7.9, 'Иваново'),
#     ('Елизавета', '14', 9.1, 'Тверь'),
#     ('Дмитрий', '12', 5,2, 'Челябинск'),
#     ('Максим', '15', 6.1, 'Самара'),
#     ('Николай', '11', 8.7, 'Владивосток'),
#     ('Артур', '13', 5.8, 'Екатеринбург'),
#     ('John', '13', 10, 'WinterFell')
# )
# total_mark = 0
# for student in students:
#     total_mark += student[2]
# # print(total_mark)   

# avg_mark = total_mark / len(students)
# print(avg_mark)
# good_students = []
# for student in students:
#     if student[2] > avg_mark:
#         good_students.append(student[0])        
# print(f'Ученики {good_students} в этом семестре хорошо учатся!')

    























