## 适合把一些pdg的文件转换并且合并为pdf文档。
## https://prahladyeri.github.io/blog/2019/10/python-recipe-combine-images-pdf.html
import os, glob
from PIL import Image
from fpdf import FPDF

## 目录的名字，不能有空格。##############################
sdir = '/Users/minkexiu/Downloads/To_disk/汉服款式设计与表现_丁雯编著_zhelper-search/'
#####################################################
w,h = 0,0

for i in os.listdir(sdir):
    os.system(f"cp {(sdir + i)} {(sdir + i).replace('.pdg', '.jpg')}")

## legs and covs. All files
legs = sorted(glob.glob(sdir + "leg*.jpg"))
covs = sorted(glob.glob(sdir + "cov*.jpg"))
all_files = sorted(glob.glob(sdir + "*.jpg"))

## initialize the file.
cover = Image.open(covs[0]) # os.path.join(sdir, "cov001.jpg")
w,h = cover.size
pdf = FPDF(unit = "pt", format = [w,h])
image = covs[0]
pdf.add_page()
pdf.image(image,0,0,w,h)

def add_page(image_path):
    pdf.add_page()
    pdf.image(image_path,0,0,w,h)

## bok.
boks = sorted(glob.glob(sdir + "bok*.jpg"))
for bok in boks:
    add_page(bok)

## catalogue.
catalogue = sorted(glob.glob(sdir + "!*.jpg"))
for ct in catalogue:
    add_page(ct)

## 正文
contents = sorted(list(set(all_files) - set(legs) - set(covs) - set(boks) - set(catalogue)))
for ctt in contents:
    add_page(ctt)

## legs，剩下的cov
for leg in legs:
    add_page(leg)
for cv in covs[1:]:
    add_page(cv)

pdf.output("output.pdf", "F")