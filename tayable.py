"""

A module that contains classes, functions and utilties for
converting a html table into yaml.

This is used as an helper for a textmate bundle to convert
html tables in legacy pages to yaml data to use with hyde.
"""

from itertools import izip
from pyquery import PyQuery
import yaml

__version__ = '0.0.1a'

def convert(frag):
    """
    Convert the provided html fragment into yaml data.
    The data would be "interesting" if you have:
    - nested tables
    - colspans
    - no th items

    Converts the first table element found in the given
    fragment.

    Returned yaml has the following strucuter:

    columns:
        -   col1 #(column header)
        -   col2

    rows:
        -
            col1: value
            col2: 12345
    """
    q = PyQuery(frag)
    table = q('table').eq(0)

    columns = [th.text for th in table.find('th')]
    if not columns:
        return {}

    trs = table.find('tr')

    def make_row(tr):
        return dict([(col, val.text)
                    for col, val in
                        izip(columns, tr.iterchildren('td'))])

    rows = [make_row(tr) for tr in trs]

    return yaml.dump({"columns":columns, "rows": rows})


class TestConvert(object):
    """
    Tests for html to yaml conversion.
    """

    def test_basic_table(self):
        table = """
<table>
    <thead>
        <th>Column One</th>
        <th>Column Two</th>
    </thead>
    <tbody>
        <tr>
            <td>123</td>
            <td>ABC</td>
        </tr>
        <tr>
            <td>890</td>
            <td>XYZ</td>
        </tr>
    </tbody>
</table>
"""

        expected = """
columns:
    - Column One
    - Column Two
rows:
    -
        Column One: '123'
        Column Two: ABC
    -
        Column One: '890'
        Column Two: XYZ
"""
        out = convert(table)
        assert out
        y = yaml.load(out)
        assert y
        e = yaml.load(expected)
        print y
        print e
        assert yaml.dump(y) == yaml.dump(e)



