import csv
import requests
from datetime import datetime


class csvParser:
    def __init__(
        self,
        csv_file_name,
    ):
        self._csv_file_name = csv_file_name

    @property
    def csv_file_name(self):
        return self._csv_file_name

    def csv_parser(self):
        parsed_results = []
        with open(self.csv_file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                _, txid, _, amount, _, address = row
                parsed_results.append(self.output_parser(
                    txid, amount, address))
        return parsed_results

    def output_parser(
        self,
        txid,
        amount,
        address,
    ):
        response = requests.get(f'https://blockchain.info/rawtx/{txid}').json()
        creation_time = str(datetime.fromtimestamp(response['time']))

        utxo_data = {
            'amount': amount,
            'address': address,
            'creation_time': creation_time
        }
        return utxo_data
