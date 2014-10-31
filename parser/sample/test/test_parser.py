import unittest

from parser.sample.sample_parser import Parser


class TestPhysicalLocationInstanceParser(unittest.TestCase):
    def setUp(self):
        self.__parser = Parser()

    def test_case_1(self):
        text = '- aaa AAAA + ABC ( 135325 3824500 ) A ;'
        expect = {'ABC': (135325, 3824500, 'A'), 'mem_data': ('aaa', 'AAAA')}
        result = self.__parser.parse(text)
        self.assertDictEqual(result, expect)

    def test_case_2(self):
        text = '- aaa/bbb CBA + FOX ( 0 120000 ) Z ;'
        expect = {'FOX': (0, 120000, 'Z'), 'mem_data': ('aaa/bbb', 'CBA')}
        result = self.__parser.parse(text)
        self.assertDictEqual(result, expect)

    def test_case_3(self):
        text = '- aaa/ddd/ccc XXX + WWWW DIST + LION ( 0 2255000 ) X ;'
        expect = {'LION': (0, 2255000, 'X'), 'mem_data': ('aaa/ddd/ccc', 'XXX'),
                  'WWWW': 'DIST'}
        result = self.__parser.parse(text)
        self.assertDictEqual(result, expect)

    def test_case_4(self):
        text = '- a/b/c/d/e OAOAOA + SOURCE DIST + OED ( 0 1024000 ) Y ;'
        expect = {'OED': (0, 1024000, 'Y'), 'mem_data': ('a/b/c/d/e', 'OAOAOA'),
                  'SOURCE': 'DIST'}
        result = self.__parser.parse(text)
        self.assertDictEqual(result, expect)

    def test_case_5(self):
        text = '- a/b/c/d/e OAOAOA + UNPLACED ;'
        expect = {'mem_data': ('a/b/c/d/e', 'OAOAOA'),
                  'UNPLACED': (0, 0, '')}
        result = self.__parser.parse(text)
        self.assertDictEqual(result, expect)

    def test_case_6(self):
        text = '''
                - oo/a_a/dda HJKL + ORZ ( 1242471 7886393 ) FS 
                +WAIT 1 
                +HELLO 100 500 1000 2000
;
'''
        expect = {'mem_data': ('oo/a_a/dda', 'HJKL'),
                  'ORZ': (1242471, 7886393, 'FS'),
                  'WAIT': 1,
                  'HELLO':(100, 500, 1000, 2000)}
        result = self.__parser.parse(text)
        self.assertDictEqual(result, expect)

if __name__ == "__main__":
#    import sys;sys.argv = ['', 'TestPhysicalLocationInstanceParser.test_case_1']
    unittest.main()
