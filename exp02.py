import pickle

def process_pickle(path, encoding="latin1"):
    """
        Reading pickle file
        :param path: Path to a pickle file.
        :return data: Dictionary with data.
    """
    with open(path, 'rb') as handle:
        # data = pickle.load(open(path, "rb"), encoding=encoding)
        data = pickle.load(handle, encoding=encoding)
    return data

zh2en_dict = process_pickle('./data/zh2en_dict01.pkl')
print(zh2en_dict)