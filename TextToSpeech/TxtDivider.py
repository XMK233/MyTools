import os,re

filePath = r"C:\Users\XMK23\Documents\Books\杂学\细说宋朝.txt"

## read the original txt file
with open(filePath, "r", encoding="utf-8") as fp:
    lines = fp.readlines()

## delete extra empty lines
changed = []
for l in lines:
    if l in ["\n", "\u3000\u3000\n", "\u3000\n"]:
        continue
    changed.append(l)

## catch the number of title lines
lineNumbers = []
for n, l in enumerate(changed):
    res = re.search('细说宋朝\d+：', l)
    if not res:
        continue
    # print(l.strip(), n)
    lineNumbers.append(n)

## get the chapters:
chapter_folder = "chapters"
if not os.path.exists(chapter_folder):
    os.makedirs(chapter_folder)
for i in range(0, len(lineNumbers) - 1):
    chapter = changed[lineNumbers[i] + 1: lineNumbers[i + 1]]
    chapter_line = "".join([_.strip() for _ in chapter])
    with open(os.path.join(chapter_folder, changed[lineNumbers[i]].strip()) + ".txt", "w", encoding="utf-8") as f:
        f.write(chapter_line)
    # print(chapter_line)
chapter = changed[lineNumbers[-1] + 1:]
chapter_line = "".join([_.strip() for _ in chapter])
with open(os.path.join(chapter_folder, changed[lineNumbers[-1]].strip()) + ".txt", "w", encoding="utf-8") as f:
    f.write(chapter_line)
# print(chapter_line)



