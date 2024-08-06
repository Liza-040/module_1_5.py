immutable_var = (1, 2, True, [1,4], 'String', 7.4)
print(immutable_var)
immutable_var[0] = 2
# Нельзя изменить, потому что главное свойство кортежа - его неизменяемость
mutable_list = [1, 'String',True]
mutable_list[0] = 'hi'
mutable_list[-1] = False
print(mutable_list)
