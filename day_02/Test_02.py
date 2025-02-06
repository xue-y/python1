import textwrap
line1 = input().strip()
line2 = input().strip()
line3 = input().strip()

max_width = max([len(line) for line in [line1, line2, line3]])
print(max_width)
border_width = max_width + 4

border = '+' + ('-' * border_width) + '+'
def fill_text(text, width):
    filled = textwrap.fill(text, width)
    return filled.replace(' ', ' ')

print(border)

for line in [line1, line2, line3]:
    filled_line = fill_text(line, border_width)
    print(f'  {filled_line}  ')

print(border)
