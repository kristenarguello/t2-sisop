# copilot did it
class SimulateMemoryAllocator:
    def __init__(self, memory_size):
        self.memory_size = memory_size
        self.memory = [0] * memory_size

    def allocate(self, size):
        for i in range(self.memory_size - size + 1):
            if all(self.memory[i + j] == 0 for j in range(size)):
                for j in range(size):
                    self.memory[i + j] = 1
                return i
        return -1

    def deallocate(self, start, size):
        for i in range(size):
            self.memory[start + i] = 0

    def print_memory(self):
        print(self.memory)
