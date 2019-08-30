class Human():
    def __init__(self, human):
        self.human = human


class Man(Human):
    def __init__(self):
        super().__init__('Man')


class Woman(Human):
    def __init__(self):
        super().__init__('Woman')

def God():
    man = Man()
    woman = Woman()
    return [man, woman]