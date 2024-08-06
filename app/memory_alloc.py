class SimulateMemoryAllocator:
    def __init__(self, virtual_mem, physical_mem, page_size):
        self.virtual_mem_size = virtual_mem
        self.physical_mem_size = physical_mem
        self.page_size = page_size

        # uses bit manipulation
        self.num_pages = 2 ** (self.virtual_mem_size - self.page_size)
        self.num_frames = 2 ** (self.physical_mem_size - self.page_size)

        self.page_table = [-1] * self.num_pages
        self.memory = [0] * physical_mem

    def get_physical_address(self, virtual_address):
        # checks if the virtual address is within the range
        if virtual_address >= 2**self.virtual_mem_size:
            raise ValueError("Virtual address is out of range")

        # for each >> = division by 2
        # for each & = modulo by 2
        # for each << = multiplication by 2
        # for each | = addition
        page_number = virtual_address >> self.page_size
        offset = virtual_address & ((1 << self.page_size) - 1)

        if self.page_table[page_number] == -1:
            try:
                free_frame = self.memory.index(0)
            except ValueError:
                raise MemoryError("No more free frames in the physical memory")

            self.page_table[page_number] = free_frame
            self.memory[free_frame] = 1

        frame_number = self.page_table[page_number]
        return (frame_number << self.page_size) | offset  # physical address

    def simulate_list_addresses(self, virtual_addresses):
        return [
            self.get_physical_address(virtual_address)
            for virtual_address in virtual_addresses
        ]
