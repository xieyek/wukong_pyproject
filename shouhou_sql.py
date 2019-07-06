from sql import Mysql

#售后订单
def job_orders(order_id):
    sql='SELECT* FROM job_orders WHERE order_id=%d;'%order_id
    Mysql().execude_sql(sql)

job_orders(1374582)