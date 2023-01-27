import json
def read_json(file):
    f= open(file,"r")
    data = json.load(f)
    f.close()
    return data

def write_json(file, data):
    fw= open(file, "w")
    data_to_be_written = json.dumps(data, indent=3,)
    fw.write(data_to_be_written)
    fw.close()