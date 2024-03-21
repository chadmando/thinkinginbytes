from rich.console import Console
from rich.table import Table
from collections import OrderedDict
import hashlib

def hash_byte_sections_variable_block(byte_data, BLOCK_SIZE=8):
    if isinstance(byte_data, bytearray):
        byte_data = bytes(byte_data)
    hash_dict = OrderedDict()
    for i in range(0, len(byte_data), BLOCK_SIZE):
        section = byte_data[i:i+BLOCK_SIZE]
        hash_value = hashlib.sha1(section).hexdigest()
        hash_dict[(i, i+BLOCK_SIZE)] = hash_value
    return hash_dict

def compare_hashes(byte_string_1, byte_string_2, BLOCK_SIZE=8):
    hashes_1 = hash_byte_sections_variable_block(byte_string_1, BLOCK_SIZE)
    hashes_2 = hash_byte_sections_variable_block(byte_string_2, BLOCK_SIZE)
    
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Section", style="dim")
    table.add_column("Hash 1")
    table.add_column("Hash 2")
    
    sections = list(hashes_1.keys())
    for section in sections:
        hash_1 = hashes_1[section]
        hash_2 = hashes_2[section]
        table.add_row(str(section), hash_1, hash_2)
    
    console = Console()
    console.print(table)

# Example byte strings
byte_string_1 = b"The rain in Spain falls mainly on the plain."
byte_string_2 = b"Yo! The rain in Spain falls mostly on the plain."

# Comparing the hashes of the two byte strings
compare_hashes(byte_string_1, byte_string_2)
