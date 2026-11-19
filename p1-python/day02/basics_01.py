variable = "TTB-CHIPS-2026-11"
list = variable.split("-")
# print(list)
year = int(list[2])
month = int(list[3])
print(month + 1)

string = "  ttb-chips  "
clean_string = string.strip().upper()
print(clean_string)

qty=98765.4321

print(f"{qty:.2f}")

perc_value = 0.734

print(f"{perc_value:.1%}")

batch="B2026111900042"

date = batch[1:9]
sequence = batch[9:14]

alphabet = "A-B-C-D"
print(alphabet.count("-"))

string2 = "MIXER_02_TEMP"

print(string2.endswith("_TEMP"))

string3 = "Line 3 Packing Speed"

replaced_string = string3.replace(" ", "-")
print(replaced_string)

print(f"{7:03d}")

tag = None

print("UNKNOWN" if tag is None else tag)

string4 = ["TTB","CHIPS","2026"]

print(("|").join(string4))

string5 = "TTB-CHIPS-2026"

position = string5.find("CHIPS")
word = string5[position:position + len("CHIPS")]

print(word)

plant = "TTB"; line = 3; output = 12450; oee = 0.812
print(f"[{plant}] Line {line} | Output: {output:,.2f} kg | OEE: {oee:.1%}")