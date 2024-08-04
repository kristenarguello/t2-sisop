from .utils import address_transformer_str_to_bit


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
