import argparse
import json
import os


def read(file_path, fmt=None):
    """
        :param file_path: path to config file
        :param fmt: format of input file
        :return: parsed data as python structure
    """
    if not fmt:
        fmt = get_extension(file_path)
    fmt = fmt.lower()
    if fmt == 'json':
        return _read_json(file_path)
    raise NotImplementedError(f"{fmt} format is not supported yet.")


def _read_json(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        return data


def save(file_path, data, fmt):
    fmt = fmt.lower()
    if fmt == 'json':
        return _save_json(file_path, data)
    raise NotImplementedError(f"{fmt} format is not supported yet.")


def _save_json(file_path, data):
    with open(file_path, 'w') as output_file:
        json.dump(data, output_file)


def get_extension(path):
    _, ext = os.path.splitext(path)
    return ext[1:]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg_path", required=True)
    parser.add_argument("--output_path", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    json_data = read(args.cfg_path)
    save(args.output_path, json_data, 'json')


if __name__ == "__main__":
    main()
