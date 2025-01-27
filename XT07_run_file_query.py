from mysql_con import query_database
from schema import SchemaExcel


def test01():
    file_name = r'C:\Users\baido\OneDrive\Work\AI\GDH\xbbChat2Sql\xbbChat2sql_main\excel_schema\emp.xlsx'
    sql = SchemaExcel.get_sql_from_file(file_name, "我们每个部门分别有多少个员工?请按照部门名称和人数来显示")

    print("sql = " + sql)

    res = query_database.query_sql(sql)

    print(res)


def test02():
    file_name = r'C:\Users\baido\OneDrive\Work\AI\GDH\xbbChat2Sql\xbbChat2sql_main\excel_schema\hfm.xlsx'

    sql = SchemaExcel.get_sql_from_file(file_name, "请查询广东粤海控股集团有限公司2024年9月的营业利润是多少?")

    print("sql = " + sql)

    df = query_database.query_sql(sql)

    res = df.to_string()

    print(res)


if __name__ == '__main__':
    test01()
