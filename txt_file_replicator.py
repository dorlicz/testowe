import os

directory = 'dss_lists/nefy'

with open("DSS_lists/lista.txt") as input_list:
    org_text = input_list.read()

for filename in os.listdir(directory):
    name_raw = os.path.join(filename)
    with open("dss_lists/" + name_raw + ".txt", "w") as new_txt:
        input_text = org_text[:51] + name_raw + org_text[63:]
        new_txt.write(input_text)

