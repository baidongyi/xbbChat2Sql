from mysql_con import query_database


def test01():
    sql = "SELECT count(*) FROM emp"
    df = query_database.query_sql(sql)
    res = df.to_string()
    print(f"res=\n{res}")

def test02():
    sql = r"SELECT T1.dname,  COUNT(*) FROM dept AS T1 JOIN emp AS T2 ON T1.deptno  =  T2.deptno GROUP BY T1.dname"

    df = query_database.query_sql(sql)

    res = df.to_string()
    print(f"res=\n{res}")

if __name__ == '__main__':
    test02()
