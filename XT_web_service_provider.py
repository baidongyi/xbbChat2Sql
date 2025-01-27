import uvicorn
# -*- coding:utf-8 -*-
from fastapi import FastAPI
import socket

from schema import SchemaExcel
from mysql_con import query_database

app = FastAPI()


def get_answer(question:str):
    file_name = 'hfm.xlsx'
    sql = SchemaExcel.get_sql(file_name, question)

    print("sql = " + sql)

    df = query_database.query_sql(sql)

    return sql + "\n\n" + str(df)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/ask/{question}")
async def answer_question(question):
    answer = get_answer(question)
    print("Q=" + question + ", answer = " + answer)
    return {"我:": question, "小白白GPT:":answer}

@app.get("/a/{question}")
async def answer_question(question):
    answer = get_answer(question)
    print("Q=" + question + ", answer = " + answer)
    return answer

def get_my_ipv4():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return ip


if __name__ == "__main__":
    ip = get_my_ipv4()
    print("my ip = " + ip)
    uvicorn.run(app, host=ip, port=8100, workers=1)
