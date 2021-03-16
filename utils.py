import pickle

def generate_pickle(path, data):
    with open(path, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def process_pickle(path, encoding="latin1"):
    with open(path, 'rb') as handle:
        data = pickle.load(handle, encoding=encoding)
    return data