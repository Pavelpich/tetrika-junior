# Необходимо реализовать декоратор `@strict`
# Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов, объявленным в прототипе функции.
# (подсказка: аннотации типов аргументов можно получить из атрибута объекта функции `func.__annotations__` или с помощью модуля `inspect`)
# При несоответствии типов бросать исключение `TypeError`
# Гарантируется, что параметры в декорируемых функциях будут следующих типов: `bool`, `int`, `float`, `str` 
# Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию


def strict(func):
    
    def wrapper(*args):
        sign_types_list = list(func.__annotations__.values())[:-1]
        args_types_list = [type(arg) for arg in args]
        if sign_types_list == args_types_list:
            return func(*args)
        else:
            raise TypeError() # Несоответствие типов сигнатуры функции и типов переданных аргументов
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

# @

if __name__ == "__main__":
    print(sum_two(1, 2))  # >>> 3
    print(sum_two(1, 2.4))  # >>> TypeError

    #tests
    assert sum_two(1,2) == 3
    try:
        sum_two(1, 2.4)
    except TypeError:
        assert True

