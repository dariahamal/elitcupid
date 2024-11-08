def my_generator():
    yield 1
    yield 23
    yield 0.0026669225995978383

gen = my_generator()
for value in gen:
    print(value)
