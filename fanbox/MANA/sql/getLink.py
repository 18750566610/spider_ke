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


def select():

    # 执行命令（sql）
    cursor.execute("select * from id6")
    db.commit()
    tuple1 = cursor.fetchall()
    # print(list(map(list, tuple1)))
    result = list(map(list, tuple1))
    return result


if __name__ == "__main__":
    select()
