from Table_Generator import TG
import os
import json

class Database:
    def __init__(self, file="pinyin_to_hiragana_table.json"):
        self.table_file = file
        self.table = self.load_table()
        
    def load_table(self):
        if not os.path.exists(self.table_file):
            tg = TG()
            tg.generate_tables()
        
        with open(self.table_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
if __name__ == "__main__":
    db = Database()
    print(db.table)