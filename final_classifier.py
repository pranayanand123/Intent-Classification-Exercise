# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 01:17:50 2018

@author: pranay
"""
import pandas
import numpy
stri = '''accessoryif - Does it come with a scoop?
amountget - What about sugar content?
certificateif - is this product certified gluten free?
colorif - Is the Vanilla protein powder white?
containget - What kind of pea used for protein?
containif - Is this product made with Sustainable palm oil?
dayservingget - How many days supply is in the large tub?
describeget - How is this vegan if dairy is listen on the ingredients?
expiryget - Where can i find the expiration date ?
numservingget - How many total servings is included in the 30.8 oz tub?
packageif - Is the seal supposed to have 5 holes?
packagesizeget - do they make a bigger container ?
placeget - Where is this manufactured?
placeif - is the product made in the usa?
safeforif - Is this safe for pregnant women?
servingamountget - What typical measurement equals 1 scoop?
storagedurationget - How long will this keep if stored correctly? Thanks!
storagemethodif - Do i need to keep vegaone in freeze?'''
li = stri.split("\n")

listab= []
for i in li:
    a,b = i.split("-")
    listab.append([a,b])
frame2 = pandas.DataFrame(listab)

