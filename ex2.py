# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ — значение переданного аргумента, а значение — имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

def keyword_arguments_to_dict(**kwargs):
    argument_dict = {}
    for key, value in kwargs.items():
        argument_dict[value if hashable(value) else str(value)] = key
    return argument_dict

def hashable(value):
    try:
        hash(value)
        return True
    except TypeError:
        return False

result = keyword_arguments_to_dict(a=1, b="hello", c=[1, 2, 3])
print(result)