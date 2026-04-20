import pandas as pd
import json
import os

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def parse_response(response_text):
    try:
        # Clean response if needed
        text = response_text.strip()
        if "```" in text:
            text = text.split("```")[1]
            if text.startswith("json"):
                text = text[4:]
        return json.loads(text)
    except Exception as e:
        print(f"Parse error: {e}")
        return None

def export(data, filename="dataset"):
    df = pd.DataFrame(data["rows"], columns=data["columns"])
    
    paths = {}
    
    # CSV
    csv_path = f"{OUTPUT_DIR}/{filename}.csv"
    df.to_csv(csv_path, index=False)
    paths["csv"] = csv_path
    
    # JSON
    json_path = f"{OUTPUT_DIR}/{filename}.json"
    df.to_json(json_path, orient="records", indent=2)
    paths["json"] = json_path
    
    # Excel
    excel_path = f"{OUTPUT_DIR}/{filename}.xlsx"
    df.to_excel(excel_path, index=False)
    paths["excel"] = excel_path
    
    # SQL
    sql_path = f"{OUTPUT_DIR}/{filename}.sql"
    with open(sql_path, "w") as f:
        f.write(f"CREATE TABLE {filename} (\n")
        for col in data["columns"]:
            f.write(f"  {col} TEXT,\n")
        f.write(");\n\n")
        for row in data["rows"]:
            values = ", ".join([f"'{v}'" for v in row])
            f.write(f"INSERT INTO {filename} VALUES ({values});\n")
    paths["sql"] = sql_path
    
    # Text
    txt_path = f"{OUTPUT_DIR}/{filename}.txt"
    df.to_string(open(txt_path, "w"), index=False)
    paths["txt"] = txt_path
    
    return paths