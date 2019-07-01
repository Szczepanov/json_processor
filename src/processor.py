import argparse
import json


def read_config(path_to_file):
    """
        :param path_to_file: path to json config file
        :return: parsed json data as python dict
    """
    with open(path_to_file, "r") as json_file:
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
    json_data = read_config(args.cfg_path)
    print(json_data)


if __name__ == "__main__":
    main()
