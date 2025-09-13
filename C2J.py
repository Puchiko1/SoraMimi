# 中文空耳日文
from database import Database
from pypinyin import lazy_pinyin


def run():
    converted_list = lazy_pinyin(input("(按 Ctrl+C 退出) 输入文本：").strip())
    
    new_str = ""
    for char in converted_list:
        for dict in table:
            if char == dict["key"]:
                new_str += dict["to"]
                break
        if not any(char == dict["key"] for dict in table):
            new_str += char
    
    if new_str:
        print(new_str)
    
if __name__ == "__main__":
    db = Database() # 默认为平假名
    table = db.table
    while True:
        try:
            run()
        except KeyboardInterrupt:
            break
