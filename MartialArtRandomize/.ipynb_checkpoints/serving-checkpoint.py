from flask import Flask
from GenerateList import consume_list
from flask import render_template, request
from datetime import datetime
import zhdate, re
import pandas as pd

app = Flask(__name__) ## , template_folder="IpMan_Murenzhuang"

def three_num_get_gua(a, b, c):
    '''梅花易数三数起卦，以取本、互、变。'''
    bagua = ["111", "110", "101", "100", "011", "010", "001", "000"]
    guatu = {
        "111": ("☰", "天", "乾金"), 
        "110": ("☱", "泽", "兑金"),
        "101": ("☲", "火", "离火"),
        "100": ("☳" , "雷", "震木"),
        "011": ("☴", "风", "巽木"),
        "010": ("☵", "水", "坎水"),
        "001": ("☶", "山", "艮土"),
        "000": ("☷", "地", "坤土"),
    }
    ## https://zhuanlan.zhihu.com/p/457104350
    gua_64 = "乾乾天，天风姤，天山遁，天地否，风地观，山地剥，火地晋，火天大有，坎坎水，水泽节，水雷屯，水火既济，泽火革，雷火丰，地火明夷，地水师，艮艮山，山火贲，山天大畜，山泽损，火泽睽，天泽履，风则中孚，风山渐，震震雷，雷地豫，雷水解，雷风恒，地风升，水风井，泽风大过，泽雷随，巽巽风，风天小畜，风火家人，风雷益，天雷无妄，火雷噬嗑，山雷顾，山风蛊，离离火，火山旅，火风鼎，火水未济，山水蒙，风水涣，天水松，天火同人，坤坤地，地雷复，地泽临，地天泰，雷天大壮，泽天夬，水天需，水地比，兑兑泽，泽水困，泽地萃，泽山咸，水山蹇，地山谦，雷山小过，雷泽归妹"
    gua_64_dict = {x[:2]: x[2:]for x in gua_64.split("，")}
    
    shanggua_idx = 7 if (a % 8 == 0) else (a % 8 - 1)
    xiagua_idx = 7 if (b % 8 == 0) else (b % 8 - 1)
    bianyao_idx = 5 if (c % 6 == 0) else (c % 6 - 1)
    bengua = bagua[xiagua_idx] + bagua[shanggua_idx]
    hugua = bengua[1:-1][:3] + bengua[1:-1][1:]
    biangua = list(bengua)
    biangua[bianyao_idx] = str(1 - int(biangua[bianyao_idx]))
    biangua = "".join(biangua)
    df = pd.DataFrame([[
        guatu[bengua[3:]][0]+guatu[bengua[3:]][2], guatu[hugua[3:]][0]+guatu[hugua[3:]][2], guatu[biangua[3:]][0]+guatu[biangua[3:]][2], 
    ],[
        guatu[bengua[:3]][0]+guatu[bengua[:3]][2], guatu[hugua[:3]][0]+guatu[hugua[:3]][2], guatu[biangua[:3]][0]+guatu[biangua[:3]][2], 
    ]], index=["上卦", "下卦"], columns = [
        guatu[bengua[3:]][1] + guatu[bengua[:3]][1] + gua_64_dict[guatu[bengua[3:]][1] + guatu[bengua[:3]][1]],
        guatu[hugua[3:]][1] + guatu[hugua[:3]][1] + gua_64_dict[guatu[hugua[3:]][1] + guatu[hugua[:3]][1]],
        guatu[biangua[3:]][1] + guatu[biangua[:3]][1] + gua_64_dict[guatu[biangua[3:]][1] + guatu[biangua[:3]][1]],
    ])    
    return df

def easy_start_gua_lunar():
    '''用农历的月、日、时辰来起卦。'''
    time_now = datetime.now()
    zh_date_str = str(zhdate.ZhDate.from_datetime(time_now))
    zh_date_str_1 = datetime.strftime(
        datetime(
            *[int(x) for x in re.findall("\d+", zh_date_str)]
        ),
        '%Y-%m-%d'
    )
    zh_hour = (time_now.hour + 1)//2%12+1
    zh_hour_dizhi = "子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥".split("、")[zh_hour-1]
    
    n1, n2, n3 = zh_date_str_1[5:7], zh_date_str_1[8:10], zh_hour
    print(n1, n2, n3, f"{zh_hour_dizhi}时")
    return three_num_get_gua(int(n1), int(n2), int(n3))


@app.route('/')
def hello_world():
    return render_template("welcome.html")  ## 'Hello, Martial Art World!'

@app.route('/next')
def nextMartialArt():
    ma = consume_list()
    gua_table = easy_start_gua_lunar()
    with open("templates/current_gua.html", "w") as f:
        f.write(gua_table.to_html())
    title, up, down = gua_table.to_string().split("\n")
    return render_template("display.html", ma = ma)

@app.route('/yongchun', methods = ['GET'])
def getPage_yongchun():
    page = request.args.get("p")
    return render_template("IpMan_Murenzhuang/{}.html".format(page)) 

@app.route('/sjg', methods = ['GET'])
def getPage_sjg():
    page = request.args.get("p")
    return render_template("shuang_jie_gun_18/{}.html".format(page)) 

# ##########
# @app.route('/json')
# def json():
#     return render_template('welcome.html')

# ##background process happening without any refreshing
# @app.route('/background_process_test')
# def background_process_test():
#     print ("Hello")
#     return "nothing"

if __name__ =="__main__":
    app.run(debug=True,port=54233)