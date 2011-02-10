"""

A module that contains classes, functions and utilties for
converting a html table into yaml.

This is used as an helper for a textmate bundle to convert
html tables in legacy pages to yaml data to use with hyde.
"""

import sys
from itertools import izip
__version__ = '0.0.2a'

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
    from pyquery import PyQuery
    import yaml

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

    rows = [make_row(tr) for tr in trs if tr.findall('td')]

    return yaml.dump({"columns":columns, "rows": rows})


def main():
    html = sys.stdin.read()
    sys.stdout.write(convert(html))

if __name__ == "__main__":
    sys.exit(main())

class TestConvert(object):
    """
    Tests for html to yaml conversion.
    """

    def test_basic_table(self):
        from pyquery import PyQuery
        import yaml

        table = """
<table>
    <thead>
        <tr>
            <th>Column One</th>
            <th>Column Two</th>
        </tr>
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
        assert yaml.dump(y) == yaml.dump(e)