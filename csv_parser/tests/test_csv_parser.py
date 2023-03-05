import os
import sys
import pytest

try:
    import csv_parser
except ModuleNotFoundError:
    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, parent_dir)
    import csv_parser


def test_csv_parser():
    parser = csv_parser.csvParser('test.csv')
    assert parser.csv_parser() == [
        {
            'amount': '9466355',
            'address': '1LpCmEejWLNfZigApMPwUY9nZTS8NTJCNS',
            'creation_time': '2012-07-19 23:51:39'
        },
        {
            'amount': '339500',
            'address': '1FuphZ7xVPGrxthQT1S8X7nNQNByYxAT3V',
            'creation_time': '2018-07-21 00:10:43'
        },
        {
            'amount': '300000',
            'address': '18Y9yhjU9g2jjJmvaUy7TmUNZH9iPzQ4dd',
            'creation_time': '2017-01-11 16:13:46'
        },
        {
            'amount': '100000',
            'address': '1EKHTvovYWHfUJ6i9vsoidyTPQauCPH1qC',
            'creation_time': '2017-11-04 17:18:25'
        },
        {
            'amount': '27668',
            'address': '1fkEhLpPKdmKtaxKdp4yDp1c87dF7GDub',
            'creation_time': '2017-11-05 13:09:08'
        },
        {
            'amount': '32000',
            'address': '15KmfJcGNfL29vpsSJ37uPzTQfr8Qe17Gq',
            'creation_time': '2012-07-22 02:56:40'
        },
        {
            'amount': '41936',
            'address': '17up1oPxBMTfZdehzy4v81KzLRHGDNX8ff',
            'creation_time': '2019-03-01 05:06:59'
        },
        {
            'amount': '4528208',
            'address': '1P6Ae7unrSjtx9J5SjWuwAdZBoWcbcjzBZ',
            'creation_time': '2016-03-18 07:56:50'
        },
    ]


def test_output_parser():
    parser = csv_parser.csvParser('test.csv')
    assert (parser.output_parser(
        "033e83e3204b0cc28724e147f6fd140529b2537249f9c61c9de9972750030000",
        65279,
        "1KaPHfvVWNZADup3Yc26SfVdkTDvvHySVX",
    ) == {
        'address': '1KaPHfvVWNZADup3Yc26SfVdkTDvvHySVX',
        'amount': 65279,
        'creation_time': '2017-07-12 10:13:26',
    })


if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
