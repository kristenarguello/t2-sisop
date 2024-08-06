class SimulateMemoryAllocator:
    def __init__(self, virtual_mem, physical_mem, page_size):
        self.virtual_mem_size = virtual_mem
        self.physical_mem_size = physical_mem
        self.page_size = page_size

        # uses bit manipulation
        self.num_pages = 2 ** (self.virtual_mem_size - self.page_size)
        self.num_frames = 2 ** (self.physical_mem_size - self.page_size)

        # creates a list of -1s with the size of the number of pages to represent the page table (virtual memory)
        self.page_table = [-1] * self.num_pages
        # creates a list of 0s with the size of the number of frames to represent the physical memory
        self.memory = [0] * self.num_frames

    def get_physical_address(self, virtual_address):
        # checks if the virtual address is within the range of the virtual memory size
        if virtual_address >= 2**self.virtual_mem_size:
            raise ValueError("Virtual address is out of range")

        # >> = division
        # & = modulo
        # << = multiplication
        # | = addition
        page_number = virtual_address >> self.page_size  # gets the page number
        mask = (1 << self.page_size) - 1
        offset = virtual_address & mask  # gets the offset

        # gets the value in the page table position to the page number
        frame_number = self.page_table[page_number]

        # if its -1, it means that the page is not in the physical memory yet
        if frame_number == -1:
            try:
                # looks for a free frame in the physical memory
                free_frame = self.memory.index(0)
            except ValueError:
                raise MemoryError("No more free frames in the physical memory")

            # updates the page table with the free frame
            self.page_table[page_number] = free_frame
            # updates the physical memory to indicate it is being used
            self.memory[free_frame] = 1

        # physical address to be returned
        return (frame_number << self.page_size) | offset

    def simulate_list_addresses(self, virtual_addresses):
        # gets the physical address for each virtual address that is passed in the list
        return [
            self.get_physical_address(virtual_address)
            for virtual_address in virtual_addresses
        ]
