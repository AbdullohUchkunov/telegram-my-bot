import sqlite3

class Database:
    def __init__(self,db_name):
        self.conn = sqlite3.connect(db_name,check_same_thread=False)
        self.cur = self.conn.cursor()

    def get_all_product_by_uz(self):
        self.cur.execute("""SELECT id,name_uz FROM main""")
        product = dict_fetchall(self.cur)
        return product
    def get_all_product_by_rus(self):
        self.cur.execute("""SELECT id,name_ru FROM main""")
        product = dict_fetchall(self.cur)
        return product
    def get_all_product_by_eng(self):
        self.cur.execute("""SELECT id,name_eng FROM main""")
        product = dict_fetchall(self.cur)
        return product

    def get_all_main_2_uz(self,id_uz):
        self.cur.execute("""SELECT type_id,type_uz FROM main_2 WHERE main_id=?""",(id_uz,))
        main_2 = dict_fetchall(self.cur)
        return main_2
    def get_all_main_2_ru(self,id_ru):
        self.cur.execute("""SELECT type_id,type_ru FROM main_2 WHERE main_id=?""",(id_ru,))
        main_2 = dict_fetchall(self.cur)
        return main_2
    def get_all_main_2_eng(self,id_eng):
        self.cur.execute("""SELECT type_id,type_eng FROM main_2 WHERE main_id=?""",(id_eng,))
        main_2 = dict_fetchall(self.cur)
        return main_2

    def get_all_main_3(self,id_1):
        self.cur.execute("""SELECT * FROM main_3 WHERE main_2_id=?""",(id_1,))
        main_3 = dict_fetchall(self.cur)
        return main_3

def dict_fetchall(cursor):
    columns = [i[0] for i in cursor.description]
    return [dict(zip(columns,row))for row in cursor.fetchall()]


