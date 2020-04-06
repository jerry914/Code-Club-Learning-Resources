 #!/bin/python3

items = [
"A: 3公升的水",
"B: 洗髮精",
"C: 備用的太空服",
"D: 一把鏟子",
"E: 10天的氧氣供應",
"F:太陽能電池板",
"G: 執行任務的種子",
"H: 執行任務的土壤",
"I: 三天的食物"
]

print("現在是2049年。您要單獨執行一個任務，要在月球的基地上放滿土壤和種子，以種植更多的植物。")
print("您剛剛降落，但是遇到了麻煩。您已經離月球基地有300公里遠！")
print("您可以用3天的時間搭乘月球車到達基地")
print("月球車只能容納您的太空服和其他4個物品")
print("下面的物品中，您要帶哪些？ \n")

for objects in items:
    print(objects)

print("輸入使用逗號分隔的4個項目的代表字母。不要添加空格 \n Ex: A,B,C,D")
user_choice = input(">>> ")

user_list =  list(user_choice.split(','))
#print(user_list)

#如果用戶輸入錯誤，請告訴他們選擇中所缺少的項目
if "A" not in user_list:
  print("每天沒有喝一升水，您會脫水")

if "E" not in user_list:
  print("沒有氧氣，您將沒有空氣可以呼吸！")

if "F" not in user_list:
  print("沒有太陽能板，您的月球漫遊車將沒有足夠的動力抵達基地")

if "I" not in user_list:
  print("儘管沒有食物您可能可以生存三天，但您將需要精力來駕駛月球車。沒有食物您將無法生存。")

#告訴用戶是否可以安全抵達
if "A" in user_list and "E" in user_list and "F" in user_list and "I" in user_list:
  print("萬歲！您選擇了正確的4個項目。您將安全地抵達月球基地")
else:
  print("您沒有選擇正確的4件物品來生存。您不會安全地抵達月球基地。")
