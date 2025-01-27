from schema.SchemaDatabase import SchemaDatabase
from schema.SchemaField import SchemaField
from schema.SchemaForeignKey import SchemaForeignKey
from schema.SchemaTable import SchemaTable
from schema.SchemaTask import SchemaTask


def test01():
    f1 = SchemaField("deptno", "int")
    print(f1)


def test02():
    f1 = SchemaForeignKey("deptno", "emp", "deptno")
    print(f1)


def test11():
    f0 = SchemaField("pid", "int")
    f1 = SchemaField("name", "text")
    f2 = SchemaField("price", "int")

    t1 = SchemaTable("my_table", "pid")
    t1.set_fields([f0, f1, f2])

    print(t1)


def test12():
    f0 = SchemaField("pid", "int")
    f1 = SchemaField("name", "text")
    f2 = SchemaField("price", "int")

    t1 = SchemaTable("my_table", "pid")
    t1.set_fields([f0, f1, f2])

    print(t1)


def test21():
    f0 = SchemaField("deptno", "int")
    f1 = SchemaField("dname", "text")
    f2 = SchemaField("place", "text")

    t1 = SchemaTable("dept", "deptno")
    t1.set_fields([f0, f1, f2])

    print(t1)

    f10 = SchemaField("empno", "int")
    f11 = SchemaField("ename", "text")
    f12 = SchemaField("age", "int")
    t2 = SchemaTable("emp", "empno")
    t2.set_fields([f10, f11, f12])

    f21 = SchemaForeignKey("deptno", "dept", "deptno")
    t2.add_foreign_key(f21)

    s1 = SchemaDatabase()
    s1.set_table_list([t1, t2])


def test31():
    f0 = SchemaField("deptno", "int")
    f1 = SchemaField("dname", "text")
    f2 = SchemaField("place", "text")

    t1 = SchemaTable("dept", "deptno")
    t1.set_fields([f0, f1, f2])

    print(t1)

    f10 = SchemaField("empno", "int")
    f11 = SchemaField("ename", "text")
    f12 = SchemaField("age", "int")
    t2 = SchemaTable("emp", "empno")
    t2.set_fields([f10, f11, f12])

    f21 = SchemaForeignKey("deptno", "dept", "deptno")
    t2.add_foreign_key(f21)

    s1 = SchemaDatabase()
    s1.set_table_list([t1, t2])

    t1 = SchemaTask(s1,"每个部门的员工人数有多少?请显示部门名称和人数")

    print(t1.get_sql())


if __name__ == '__main__':
    test31()
