from utils import address_transformer_str_to_bit
from memory_alloc import SimulateMemoryAllocator

print("** MEMORY MANAGER SIMULATOR **")
virtual_mem_size = input("Enter the virtual memory size: 2^")
virtual_mem_size = int(virtual_mem_size)

physical_mem_size = input("Enter the physical memory size: 2^")
physical_mem_size = int(physical_mem_size)

page_size = input("Enter the page size: 2^")
page_size = int(page_size)


str_virtual_addresses = input(
    "Enter the virtual addresses to be translated into the physical one (please enter them in the format '0, 1, 2, 3, 4, 5'):"
)
bits_virtual_addresses = address_transformer_str_to_bit(str_virtual_addresses)

# need to use the memory allocator
mem_alloc = SimulateMemoryAllocator(virtual_mem_size, physical_mem_size, page_size)
physical_addresses = mem_alloc.simulate_list_addresses(bits_virtual_addresses)

print("The virtual addresses are:", bits_virtual_addresses)
print("The physical addresses are:", physical_addresses)
print("The page table is:", mem_alloc.page_table)
print("The physical memory is:", mem_alloc.memory)
