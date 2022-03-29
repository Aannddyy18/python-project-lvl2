def read_data(file_path):
    if file_path.endswith('.yml') or file_path.endswith('.yaml'):
        _data = open(file_path)
        return _data.read(), 'yaml'
    if file_path.endswith('.json'):
        _data = open(file_path)
        return _data.read(), 'json'
