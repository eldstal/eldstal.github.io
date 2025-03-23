#!/usr/bin/env python3

LCD_FG = (0x27, 0x35, 0x40)
LCD_BG = (0xE8, 0xE8, 0xD0)
INTENSITIES = 16

def mix(a, b, f):
    assert(f <= 1.0)

    if type(a) == int and type(b) == int:
        return int((a*f) + (b*(1-f)))
    else:
        channels = [ mix(a[i], b[i], f) for i in range(len(a)) ]
        return tuple(channels)

def css(color):
    return f"#{color[0]:02x}{color[1]:02x}{color[2]:02x}"



print(":root {")
print(f"    --lcdfg: {css(LCD_FG)};")
print(f"    --lcdbg: {css(LCD_BG)};")
print(f"    --bg: {css(mix(LCD_BG, (0,0,0), 0.9))};")

print("")
print("    /*")
print("     * lcdpx0 is background, lcdpx15 is full intensity foreground")
print("     */")

for intensity in range(INTENSITIES):
    f = 1 - (intensity/(INTENSITIES-1))
    color = css(mix(LCD_BG, LCD_FG, f))

    print(f"    --lcdpx{intensity}: {color};")

print("}")
