import argparse
import json


def read(file_path, fmt):
    """
        :param file_path: path to config file
        :param fmt: format of input file
        :return: parsed data as python structure
    """
    fmt = fmt.lower()
    if fmt == 'json':
        return _read_json(file_path)
    raise NotImplementedError(f"{fmt} format is not supported yet.")


def _read_json(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data


def save(format):
    pass


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cfg_path", required=True)
    return parser.parse_args()


def main():
    args = parse_args()
    json_data = read(args.cfg_path, 'json')
    print(json_data)


if __name__ == "__main__":
    main()
