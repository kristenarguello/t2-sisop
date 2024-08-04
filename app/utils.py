def address_transformer_str_to_bit(value: str) -> list[int]:
    addresses = value.split(", ")
    return [(int(address)) for address in addresses]
