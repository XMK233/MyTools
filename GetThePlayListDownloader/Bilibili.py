
playListURL = "https://www.bilibili.com/video/BV1Ji4y1c76c"
numOfParts = 80

with open ("download.bat", "w") as d:
    d.write("call activate py1\n")
    for i in range(1, numOfParts + 1):
        d.write("you-get {}?p={}\n".format(playListURL, i))
    d.write("pause\n")