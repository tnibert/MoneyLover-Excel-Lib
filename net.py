from moneylover import *
import json


def ls_to_json(rowlist):
    """
    :param rowlist: list of mlRow objects
    :return: json of rowlist
    """
    data = {}
    for row in rowlist:
        data[row.id] = row_to_json(row)
    return json.dumps(data, indent=2)


def row_to_json(row):
    """
    row is an mlRow object
    return a json with the id dropped
    """

    data = {"category": row.category, "amount": row.amount, "note": row.note, "wallet": row.wallet, "currency": row.currency, "date": str(row.date)}
    return json.dumps(data)

# for testing
if __name__ == '__main__':
    test, hdr = loadMLWorkbook("sample.xlsx")
    js = ls_to_json(test)
    print(js)