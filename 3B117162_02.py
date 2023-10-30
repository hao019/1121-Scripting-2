student = {}
student = dict()

sid = input("請輸入您的學號：")
sname = input("請輸入您的姓名：")
fchina = float(input("請輸入您的國文成績:"))
fmath = float(input("請輸入您的數學成績："))
finfo = float(input("請輸入您的電腦成績："))
student = {'sid': sid, 'sname': sname, 'fchina': fchina,
           'fmath': fmath, 'finfo': finfo}

sum = round(fchina + fmath + finfo, 2)
ave = round(sum / 3, 2)

print('-' * 30)
print(f"{sname}({sid})同學您好 :\n以下是您的各科成績與分數評定")
print(f"國文 : {fchina} / 數學 : {fmath} / 電腦 : {finfo}\n總分 : {sum} / 平均 : {ave}")
print('-' * 30)

if ave > 60:
    print("成績判定 : 合格")

else:
    print("成績判定 : 不合格")
 