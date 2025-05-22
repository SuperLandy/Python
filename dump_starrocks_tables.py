import mysql.connector

# 连接到 StarRocks
conn = mysql.connector.connect(
    host='10.1.1.1',
    port=6033,
    user='root',
    password='123123123',
    database='my_db'
)
cursor = conn.cursor()

# 查询指定数据库下的所有表名
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'my_db'")
tables = cursor.fetchall()

# 打开文件用于保存表结构
with open('src.sql', 'w') as f:
    for table in tables:
        table_name = table[0]
        # 获取表的创建语句
        cursor.execute(f"SHOW CREATE TABLE `{table_name}`")
        create_table = cursor.fetchone()[1]
        # 将创建语句写入文件
        f.write(create_table + '\n\n')

# 关闭连接
cursor.close()
conn.close()
