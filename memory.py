class Memory:
    def __init__(self):
        self.memory = {"0": 10, "1": 20}  # Example memory

    def load(self, address):
        return self.memory.get(str(address), 0)

    def store(self, address, value):
        self.memory[str(address)] = value