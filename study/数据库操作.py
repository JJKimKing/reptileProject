import json
from datetime import datetime

import pymysql
from pymysql.cursors import DictCursor
import logging
from json import JSONEncoder


class DateTimeEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y_%m_%d %H:%M:%S")


con = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='erp',
    charset='utf8'
)

query_sql = '''
 select * from erp_sys_user
'''

cursor = con.cursor(cursor=DictCursor)
try:
    cursor.execute(query_sql)
    result = cursor.fetchall()
    data = json.dumps(result, indent=4, cls=DateTimeEncoder)
    print(data)
except Exception as e:
    con.rollback()
    logging.error(e)

# 实现删除数据
delete_sql = '''delete from key_info where id=%s'''

try:
    cursor.execute(delete_sql, ('2'))
    con.commit()
except Exception as e:
    con.rollback()
    logging.error(e)


# # 实现插入数据库
# insert_sql = '''
#   INSERT INTO `erp`.`key_info` (`id`, `create_by`, `create_date`, `update_by`, `update_date`, `class_name`, `KEY`, `type`, `value`)
#   VALUES (%(id)s, %(create_by)s, %(create_date)s, %(update_by)s, %(update_date)s, %(class_name)s, %(key)s, %(type)s, %(value)s);
# '''
#
# # 字典参数类型插入
# insert_params = {
#     "id": '3',
#     "create_by": None,
#     "create_date": datetime.now(),
#     "update_by": None,
#     "update_date": None,
#     "class_name": 'com.geeko.admin.system.master.Spi.JsonKeyInfoHandler',
#     "key": 'Lyanic',
#     "type": 2,
#     "value": None
# }
# try:
#     cursor.execute(insert_sql, insert_params)
#     con.commit()
# except Exception as e:
#     con.rollback()
#     logging.error(e)

# insert_sql = '''
#   INSERT INTO `erp`.`key_info` (`id`, `create_by`, `create_date`, `update_by`, `update_date`, `class_name`, `KEY`, `type`, `value`)
#   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
# '''
# # 元组参数的是%s表示占位符,并不是格式化
# insert_params = ('2', None, None, None, None, "com.geeko.admin.system.master.Spi.JsonKeyInfoHandler", 'kim', 10, None)
#
# try:
#     cursor.execute(insert_sql, insert_params)
#     con.commit()
# except Exception as e:
#     con.rollback()
#     logging.error(f'插入数据库异常,异常信息:{e}')


cursor.close()
con.close()
