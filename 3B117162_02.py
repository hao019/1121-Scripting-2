student = {}
student = dict()

a = input("請輸入您的學號：")
b = input("請輸入您的姓名：")
c = float(input("請輸入您的國文成績:"))
d = float(input("請輸入您的數學成績："))
e = float(input("請輸入您的電腦成績："))
student = {'sid': a, 'sname': b, 'fchina': c,
           'fmath': d, 'finfo': e}

sum = round(c + d + e, 2)
ave = round(sum / 3, 2)

print('-' * 30)
print(f"{student['sname']}({student['sid']}) 同學您好 : \n以下是您的各科成績與分數評定")
print("國文 : {} / 數學 : {} / 電腦 : {}"
      .format(student['fchina'], student['fmath'], student['finfo']))
print(f"總分 : {sum} / 平均 : {ave}")
print('-' * 30)

if ave > 60:
    print("成績判定 : 合格")

else:
    print("成績判定 : 不合格")
