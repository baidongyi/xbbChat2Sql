import os

import gradio as gr

from schema import SchemaExcel
from mysql_con import query_database

MY_FILE = None


def combine_data(data):

    result = " "
    for idx, line in enumerate(data):
        one_line = f"\n{idx + 1}.{line.page_content}"
        result += one_line
    return result


def get_file_by_choice(choice_name: str):
    if choice_name == 'emp':
        result = r"excel_schema/emp.xlsx"
    elif choice_name == 'hfm':
        result = r"excel_schema/hfm.xlsx"
    else:
        result = r"excel_schema/emp.xlsx"
    return result


def query_by_file(question: str, file_path: str):
    print("query by file = " + file_path)

    sql = SchemaExcel.get_sql_from_file(file_path, question)

    print(f"sql=\n{sql}")

    query_result = query_database.query_sql(sql).to_string()

    return f"使用SQL语句:{sql}\n查询结果:\n{query_result}"


def chat(prompt, history, choice):

    print(prompt)

    question = prompt['text']

    global MY_FILE

    if len(prompt['files']) > 0:
        MY_FILE = str(prompt['files'][0])

    if MY_FILE is None:
        MY_FILE = get_file_by_choice(choice)


    print("S1 query file = " + MY_FILE)

    MAX_SIZE_IN_MB = 5

    file_size = round(os.path.getsize(MY_FILE) / 1024 ** 2, 2)
    print(f"file size = {file_size}")
    if file_size <= MAX_SIZE_IN_MB:
        res = query_by_file(question, MY_FILE)
    else:
        res = f"上传的文件太大[{file_size}]M,超过限制{MAX_SIZE_IN_MB}M，无法处理"


    return res


if __name__ == "__main__":
    choice_list = ["emp","hfm"]

    demo = gr.ChatInterface(chat, multimodal=True, additional_inputs=[
        gr.Dropdown(choice_list, value=choice_list[0], label="数据库", info=" ")],
                            title="智能数据助手小白白", description="可以选择数据库，进行查询。")

    demo.launch(inbrowser=True, server_name="0.0.0.0", server_port=7865, show_error=True)

