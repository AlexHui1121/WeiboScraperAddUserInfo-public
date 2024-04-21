import json

def remove_duplicates(new_file_path):
    # Step 1: Read the data from the file
    with open(new_file_path, 'r', encoding='utf-8') as f:
        data = [json.loads(line) for line in f]

    # Step 2: Process the data (remove duplicates)
    unique_data = list({item['_id']: item for item in data}.values())

    # Step 3: Write the processed data back to the file
    with open(new_file_path, 'w', encoding='utf-8') as f:
        for item in unique_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

remove_duplicates('input\\ok_keyword_米兔运动_2023_1h_20240206034803_finished.jsonl')



# # saved no ensure_ascii
# import codecs
# import json

# def convert_to_utf8(file_path):
#     with codecs.open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
#         lines = f.readlines()

#     # Decode each line separately
#     content = [json.loads(line) for line in lines]

#     with codecs.open(file_path, 'w', encoding='utf-8') as f:
#         for item in content:
#             f.write(json.dumps(item, ensure_ascii=False) + '\n')

# convert_to_utf8('output\ok_updateduserinfo_米兔运动_2017_1h_20240130193725_finished.jsonl')

