
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline


model_path = r"..\Chat2DB-SQL-7B"
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True, torch_dtype=torch.float16, use_cache=True)
pipe = pipeline("text-generation", model=model, tokenizer=tokenizer, return_full_text=False, max_new_tokens=100)

def get_sql(text:str):
    print(text)
    response = pipe(text)[0]["generated_text"]
    return response


def test01():
    prompt = "### Database schema\n\n['CREATE TABLE \"stadium\" (\\n\"Stadium_ID\" int,\\n\"Location\" text,\\n\"Name\" text,\\n\"Capacity\" int,\\n\"Highest\" int,\\n\"Lowest\" int,\\n\"Average\" int,\\nPRIMARY KEY (\"Stadium_ID\")\\n);', 'CREATE TABLE \"singer\" (\\n\"Singer_ID\" int,\\n\"Name\" text,\\n\"Country\" text,\\n\"Song_Name\" text,\\n\"Song_release_year\" text,\\n\"Age\" int,\\n\"Is_male\" bool,\\nPRIMARY KEY (\"Singer_ID\")\\n);', 'CREATE TABLE \"concert\" (\\n\"concert_ID\" int,\\n\"concert_Name\" text,\\n\"Theme\" text,\\n\"Stadium_ID\" text,\\n\"Year\" text,\\nPRIMARY KEY (\"concert_ID\"),\\nFOREIGN KEY (\"Stadium_ID\") REFERENCES \"stadium\"(\"Stadium_ID\")\\n);', 'CREATE TABLE \"singer_in_concert\" (\\n\"concert_ID\" int,\\n\"Singer_ID\" text,\\nPRIMARY KEY (\"concert_ID\",\"Singer_ID\"),\\nFOREIGN KEY (\"concert_ID\") REFERENCES \"concert\"(\"concert_ID\"),\\nFOREIGN KEY (\"Singer_ID\") REFERENCES \"singer\"(\"Singer_ID\")\\n);']\n\n\n### Task \n\n基于提供的database schema信息，what is the oldest singer?[SQL]\n"
    print(prompt)
    response = get_sql(prompt)
    print(response)


def test02():
    prompt = "### Database schema\n\n['CREATE TABLE \"stadium\" (\\n\"Stadium_ID\" int,\\n\"Location\" text,\\n\"Name\" text,\\n\"Capacity\" int,\\n\"Highest\" int,\\n\"Lowest\" int,\\n\"Average\" int,\\nPRIMARY KEY (\"Stadium_ID\")\\n);']\n\n\n### Task \n\n基于提供的database schema信息，how many stadium do we have?[SQL]\n"
    print(prompt)
    response = get_sql(prompt)
    print(response)


if __name__ == '__main__':
    test01()

