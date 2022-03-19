def read_file(f):
    if f.endswith('.yml') or f.endswith('.yaml'):
        return f, 'yaml'
    if f.endswith('.json'):
        return f, 'json'
