# -*- coding: utf-8 -*-

# access data with json file

import json

with open("./quran.json", "r",encoding="utf-8") as f:
    data = json.load(f)

# you can access any value
# for val in data[:5]:
#     print(val["name"], end="\n")

# it save output in txt file
# with open("output.txt", "w", encoding="utf-8") as f:
#     for val in data:
#         f.write(val["name"]+"\n")
# print("exit")

# detailed values in output
# ===============================================
# with open("output.txt", "w",encoding="utf-8") as f:
#     for val in data:
#         line = f"{val["id"]}\t{val["name"]}\t{val["transliteration"]}\t{val["translation"]}\t{val["type"]}\t{val["total_verses"]}\n"
#         f.write(line)
# print("exit")
# =================================================

# if you want to get output in json file
# with open("output.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=2)

# get total verse count
total_verse = 0
for val in data:
    total_verse += val["total_verses"]

print("Total verse in The Noble Quran: ", total_verse)

macca = 0
madinah = 0
for val in data:
    if val["type"] == "meccan":
        macca += 1
    else:
        madinah += 1
print(f"Surahs count revealed in Makkah is: {macca} and in Madinah is: {madinah}.")

# count the verse revealed in city
maccanVerse = 0
madinanVerse = 0
for val in data:
    if val["type"] == "meccan":
        maccanVerse += val["total_verses"]
    else:
        madinanVerse += val["total_verses"]
print(f"Verses revealed in Makkah {maccanVerse} and verses revealed in Madinah {madinanVerse}")

# it will get you details of surah revealed in Makkah or Madinah and save in chapterType.txt
# with open("chapterType.txt", "a",encoding="utf-8") as f:
#     f.write("Below are list of chapters revealed in Makkah:\n")
#     # medinan, meccan
#     for val in data:
#         if val["type"] == "meccan":
#             line = f"{val["id"]}\t{val["name"]}\t{val["translation"]} \n"
#             f.write(line)
# print("exit")