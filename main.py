INDENTS = 4
OUTPUT_NAME = "main_custom_scaled.css"

output = open(OUTPUT_NAME, "w")
scale_factor = float(input("Enter the font scale factor (Original is 1) - "))

with open("main_custom.css", encoding="utf8") as css:
    css_text = css.readlines()
for line in css_text:
    if "font-size:" in line and "px" in line:
        size = float(line[line.index(":")+2:line.index("p")])
        filtered = line[line.index("x")+1:]
        modified_line = " " * INDENTS + f"font-size: {int(round(size * scale_factor, 0))}px" + filtered
        if not modified_line.strip("\n").endswith(";"):
            output.write(modified_line[:1] + ";" + modified_line[len(modified_line):])
        else:
            output.write(modified_line)
    else:
        output.write(line)

print(f"Font Scale: {scale_factor}x\n"
      f"Saved to {OUTPUT_NAME}")
