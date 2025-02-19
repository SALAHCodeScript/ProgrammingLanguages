#!/usr/bin/python3.13
from rich.console import Console
from rich.color import ANSI_COLOR_NAMES

console = Console()

hex_numbers = [
    # from 0 to 70
    0x0,  0x1,  0x2,  0x3,  0x4,  0x5,  0x6,  0x7,  0x8,  0x9,
    0xa, 0xb, 0xc, 0xd, 0xe, 0xf,
    0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18, 0x19,
    0x1a, 0x1b, 0x1c, 0x1d, 0x1e, 0x1f,
    0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29,
    0x2a, 0x2b, 0x2c, 0x2d, 0x2e, 0x2f,
    0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39,
    0x3a, 0x3b, 0x3c, 0x3d, 0x3e, 0x3f,
    0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46
]
space_length = max([len(hex(item)) for item in hex_numbers])
for hex_value in hex_numbers:
    space = ' ' * (space_length - len(hex(hex_value)))
    print(f"{hex(hex_value)}:{space} {hex_value}")

range_list = [i for i in range(70)]
hex_numbers = [hex(h) for h in range_list]
space_length = max([len(item) for item in hex_numbers])
for i in range(len(range_list)):
    space = ' ' * (space_length - len(hex_numbers[index]))
    print(f"{hex_numbers[index]}:{space} {range_list[index]}")

range_list = [i for i in range(10001, 15000+1)]
hex_char = [rf"\{h}" for h in range_list]
space_length = max([len(item) for item in hex_char])
for i in range(len(range_list)):
    space = ' ' * (space_length - len(hex_char[index]))
    print(f"{hex_char[index]}:{space} {chr(range_list[index])}")

range_list = [i for i in range(33, 126+1)]
all_colors = [color for color in ANSI_COLOR_NAMES] 
colors = []
index = 0
for _ in range(len(range_list)):
    if all_colors[index] == all_colors[-1]:
        index = 0
    colors.append(all_colors[index])
    index += 1
hex_char = [rf"\u00{h}" for h in range_list]
space_length = max([len(item) for item in hex_char])
for index in range(len(range_list)):
    space = ' ' * (space_length - len(hex_char[index]))
    display = f"[{colors[index]}]{hex_char[index]}:{space}[/] [{colors[index*(-1)]}]{chr(range_list[index])}[/]"
    if chr(range_list[index]) != f"{chr(range_list[index])}[/]":
        display = f"[{colors[index]}]{hex_char[index]}:{space}[/] [{colors[index*(-1)]}]{chr(range_list[index])}\0[/]"
    console.print(display)
console.print(f"\n[green1]Total:[/] {len(range_list)}")

