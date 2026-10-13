class PrintMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(
            f"Создан объект класса {self.__class__.__name__} "
            f"с параметрами: {args}, {kwargs}"
        )
