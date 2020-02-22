import json
import copy


def decode_json(path):
    """ (str) -> dict
    Decode json file into a dictionary
    """
    with open(path, 'r', encoding='UTF-8') as f:
        decode_data = json.load(f)
    return decode_data


def parse_json(data):
    """ (dict) -> None
    Parse dictionary with user input
    """
    operation_data = copy.deepcopy(data)
    while True:
        options = ""
        if type(operation_data) == dict:
            for el in operation_data.keys():
                if type(el) == list:
                    options += "<масив довжиною %s>. " \
                               "Вкажіть номер від 0 до %s" \
                               % (len(el), len(el) - 1)
                else:
                    options += str(el) + ", "
        elif type(operation_data) == list:
            options = "<масив довжиною %s>. Вкажіть номер від 0 до %s, " \
                      % (len(operation_data), len(operation_data) - 1)
        else:
            print("Шуканий елемент:", operation_data)
            return
        print("Доступні опції вибору: " + options[:-2])

        chosen = input("Введіть ключ з переліку вище: ")

        try:
            try:
                chosen = int(chosen)
            except:
                pass
            operation_data = operation_data[chosen]
        except:
            print("Введено неправильний ключ! "
                  "Спробуйте ще раз!")


if __name__ == "__main__":
    output = decode_json("friends.json")
    parse_json(output)
