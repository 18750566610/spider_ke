import fanbox.MANA.sql.DOWNLOAD as SQL

def serach():
    artists_count = SQL.SQL_Select()
    for i in artists_count:
        print("共有%d位画师" % i[0])

def DELETE():
    SQL.SQL_Delete()
    artists_count = SQL.SQL_Select()
    for i in artists_count:
        print("共有%d位画师" % i[0])
if __name__ == "__main__":
    # serach()
    DELETE()
