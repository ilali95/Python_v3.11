import sys

data = [2, 'hello', 3.14, True, False, [1, 2, 3]]

for i, item in enumerate(data, start=1):
    print(f"{i}. Значение: {item}")
    print(f"   Адрес: {hex(id(item))}")
    print(f"   Размер: {sys.getsizeof(item)} байт")
    print(f"   Хэш: {hash(item)}")
    if isinstance(item, int) and item > 0:
        print("   Является положительным целым числом")
    if isinstance(item, str) and item:
        print("   Является непустой строкой")
