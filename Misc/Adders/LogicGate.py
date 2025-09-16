# (1) LogicGate
# (2) DoubleGate | SingleGate
# (3) SingleGate -> NotGate
# (3) DoubleGate -> XOrGate | AndGate | OrGate
class LogicGate():
    def __init__(self, lbl):
        self.label = lbl
    def get_lbl(self):
        return self.label
class SingleGate(LogicGate):
    def __init__(self, lbl, a):
        super().__init__(lbl)
        self.one = a
    def get_one(self):
        return self.one
class DoubleGate(LogicGate):
    def __init__(self, lbl, a, b):
        super().__init__(lbl)
        self.one = a
        self.two = b
    def get_one(self):
        return self.one
    def get_two(self):
        return self.two
    def get_output(self):
        raise NotImplementedError("Please implement get_output()")
class AndGate(DoubleGate):
    def __init__(self, lbl, a, b):
        super().__init__(lbl, a, b)
    def get_output(self):
        return 1 if self.one == self.two and self.one == 1 else 0
class OrGate(DoubleGate):
    def __init__(self, lbl, a, b):
        super().__init__(lbl, a, b)
    def get_output(self):
        return 1 if self.one == 1 or self.two == 1 else 0
class NotGate(SingleGate):
    def __init__(self, lbl, a):
        super().__init__(lbl, a)
    def get_output(self):
        return 1 if self.one == 0 else 0
class XOrGate(DoubleGate):
    def __init__(self, lbl, a, b):
        super().__init__(lbl,a,b)
    def get_output(self):
        return 1 if self.one + self.two == 1 else 0
class Connection():
    def __init__(self, s, t):
        self.source = s
        self.target = t
