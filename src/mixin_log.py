class MixinLog:

    def __init__(self):
        print(repr(self))

    def __repr__(self) -> str:
        str_list = [str(type(self).__name__) + ' (']
        for key, val in self.__dict__.items():
            str_list.append(str(val))
            str_list.append(', ')
        str_list.pop()
        str_list.append(')')
        result = ' '.join(str_list)
        return result
