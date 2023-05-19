# neostocks-tg
An example of a Python code for practicing web scraping.  
neopets stock + tg bot  

## Quick start
install requirements:  
```shell
pip install -r requirements.txt  
```

## Configuring
All configurations should be made to the ticker.txt file.  
You can set the stock ticker symbols you want to track.  

### List Neopain Companies
```shell
AAVL  
ACFI  
BB  
BOTT  
BUZZ  
CHIA  
CHPS  
COFL  
CYBU  
DROO  
EEEEE  
FAER  
FISH  
HELT  
HUW  
KAUF  
KBAT  
KSON  
LDSC  
LUPE  
MPC  
MYNC  
NAKR  
NATN  
PDSS  
PEOP  
POWR  
SHRX  
SKBD  
SKEI  
SMUG  
SSS  
STFP  
SWNC  
TAG  
TNAH  
TNPT  
TPEG  
TPP  
TSRC  
UNIB  
VPTS  
YIPP  
NEODAQ  
```

## How to use
```shell
python neostocks.py case
```

`case` The variable can be entered from 0 to 3.   
- `0`: Read ticker from txt.  
- `1`: Hot ticker.  
- `2`: Ticker price [ 15 ~ 20 ].  
- `3`: All ticker.  