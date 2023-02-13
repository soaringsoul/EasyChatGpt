import json


def read_json(json_filepath):
    with open(r"%s" % json_filepath, 'r',encoding='utf8') as f_str:
        obj_json = json.load(f_str)
    return obj_json


def write_json(json_filepath, _dict):
    with open(json_filepath, 'w', encoding='utf8') as f:
        f.write(json.dumps(_dict, indent=4))
