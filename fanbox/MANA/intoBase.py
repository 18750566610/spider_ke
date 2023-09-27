import pymysql



db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='kemono_id',
    charset='utf8')

# 获取游标
cursor = db.cursor()


def insert():
    while True:
        id = input("请输入作者id")
        company = str(input("请输入对应平台"))
        name = str(input("请输入作者名字"))
        name = f"{name}"
        company = f"{company}"
        data1 = (name, id, company)
        sql1 = '''
        insert into id6(name, id, company) value("%s","%s","%s")
        '''

        # 执行命令（sql）
        cursor.execute(sql1 % data1)
        db.commit()
        print("insert success \n")


def select():
    pass


def delete():
    pass


if __name__ == "__main__":
        insert()
