import random, sys
def generate_list():
    with open("MartialArtList.pts", "r", encoding="utf-8") as ma:
        contents = ma.readlines()
    random.shuffle(contents)
    with open("ThisRound.pts", "w", encoding="utf-8") as tr:
        for content in contents:
            tr.write("{}\n".format(content.strip()))
def consume_list():
    target = None
    ## 
    with open("ThisRound.pts", "r", encoding="utf-8") as tr:
        contents = tr.readlines()
        if contents == []:
            generate_list()
    ## output the first one. 
    with open("ThisRound.pts", "r", encoding="utf-8") as tr:
        contents = tr.readlines()    
        _ = contents[0]
        target = _.strip()
        print(target)
    ## 
    with open("ThisRound.pts", "w", encoding="utf-8") as tr:
        for content in contents:
            if content.strip() == target:
                continue
            tr.write("{}\n".format(content.strip()))

while True:
    consume_list()
    ch = input()
    # print(int(ch))
    print(ch)
    if ch == "q":
        break

# while True: 
#     consume_list()
#     ch = sys.stdin.read(1) 
#     if ch == '\x1b': 
#      exit(0) 

