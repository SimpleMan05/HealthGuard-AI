class MemoryManager:
    def __init__(self):
        self.history = []

    def add(self, message):
        self.history.append(message)

    def get_history(self):
        return self.history
