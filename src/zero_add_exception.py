class ZeroAddException(ValueError):

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else 'Попытка добавления значения 0(ноль)'

    def __str__(self):
        return self.message
