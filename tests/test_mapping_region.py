'''mapping_region unit tests'''

import unittest
from T5_worldgen.mapping_region import Sector, Subsector
from T5_worldgen.system import System


class TestAdjacentHexes(unittest.TestCase):
    '''Test nearby hex method'''
    def test_nearby_hex_1_even(self):
        '''Test 1-hex adjacency even'''
        sector = Sector('Sector')
        radius = 1
        hex_id = '1213'
        nearby_hexes = ['1113', '1114', '1212', '1214', '1313', '1314']
        print 'hex_id:', hex_id
        print 'actual:', set(sorted(nearby_hexes))
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_1_odd(self):
        '''Test 1-hex adjacency odd'''
        sector = Sector('Sector')
        radius = 1
        hex_id = '1120'
        nearby_hexes = ['1019', '1020', '1119', '1121', '1219', '1220']
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_2_even(self):
        '''Test 2-hex adjacency even'''
        sector = Sector('Sector')
        radius = 2
        hex_id = '1213'
        nearby_hexes = [
            '1012', '1013', '1014',
            '1112', '1113', '1114', '1115',
            '1211', '1212', '1214', '1215',
            '1312', '1313', '1314', '1315',
            '1412', '1413', '1414'
        ]
        print 'hex_id:', hex_id
        print 'actual:', set(sorted(nearby_hexes))
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_2_odd(self):
        '''Test 2-hex adjacency odd'''
        sector = Sector('Sector')
        radius = 2
        hex_id = '1120'
        nearby_hexes = [
            '0919', '0920', '0921',
            '1018', '1019', '1020', '1021',
            '1118', '1119', '1121', '1122',
            '1218', '1219', '1220', '1221',
            '1319', '1320', '1321'
        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )
    def test_nearby_hex_3_even(self):
        '''Test 3-hex adjacency even'''
        sector = Sector('Sector')
        radius = 3
        hex_id = '1213'
        nearby_hexes = [
            '0912', '0913', '0914', '0915',
            '1011', '1012', '1013', '1014', '1015',
            '1111', '1112', '1113', '1114', '1115', '1116',
            '1210', '1211', '1212', '1214', '1215', '1216',
            '1311', '1312', '1313', '1314', '1315', '1316',
            '1411', '1412', '1413', '1414', '1415',
            '1512', '1513', '1514', '1515'
        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_3_odd(self):
        '''Test 3-hex adjacency odd'''
        sector = Sector('Sector')
        radius = 3
        hex_id = '1120'
        nearby_hexes = [
            '0818', '0819', '0820', '0821',
            '0918', '0919', '0920', '0921', '0922',
            '1017', '1018', '1019', '1020', '1021', '1022',
            '1117', '1118', '1119', '1121', '1122', '1123',
            '1217', '1218', '1219', '1220', '1221', '1222',
            '1318', '1319', '1320', '1321', '1322',
            '1418', '1419', '1420', '1421'

        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_4_even(self):
        '''Test 4-hex adjacency even'''
        sector = Sector('Sector')
        radius = 4
        hex_id = '1213'
        nearby_hexes = [
            '0811', '0812', '0813', '0814', '0815',
            '0911', '0912', '0913', '0914', '0915', '0916',
            '1010', '1011', '1012', '1013', '1014', '1015', '1016',
            '1110', '1111', '1112', '1113', '1114', '1115', '1116', '1117',
            '1209', '1210', '1211', '1212', '1214', '1215', '1216', '1217',
            '1310', '1311', '1312', '1313', '1314', '1315', '1316', '1317',
            '1410', '1411', '1412', '1413', '1414', '1415', '1416',
            '1511', '1512', '1513', '1514', '1515', '1516',
            '1611', '1612', '1613', '1614', '1615'
        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_4_odd(self):
        '''Test 4-hex adjacency odd'''
        sector = Sector('Sector')
        radius = 4
        hex_id = '1120'
        nearby_hexes = [
            '0718', '0719', '0720', '0721', '0722',
            '0817', '0818', '0819', '0820', '0821', '0822',
            '0917', '0918', '0919', '0920', '0921', '0922', '0923',
            '1016', '1017', '1018', '1019', '1020', '1021', '1022', '1023',
            '1116', '1117', '1118', '1119', '1121', '1122', '1123', '1124',
            '1216', '1217', '1218', '1219', '1220', '1221', '1222', '1223',
            '1317', '1318', '1319', '1320', '1321', '1322', '1323',
            '1417', '1418', '1419', '1420', '1421', '1422',
            '1518', '1519', '1520', '1521', '1522'

        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_5_even(self):
        '''Test 5-hex adjacency even'''
        sector = Sector('Sector')
        radius = 5
        hex_id = '1213'
        nearby_hexes = [
            '0711', '0712', '0713', '0714', '0715', '0716',
            '0810', '0811', '0812', '0813', '0814', '0815', '0816',
            '0910', '0911', '0912', '0913', '0914', '0915', '0916', '0917',
            '1009', '1010', '1011', '1012', '1013', '1014', '1015', '1016', '1017',
            '1109', '1110', '1111', '1112', '1113', '1114', '1115', '1116', '1117', '1118',
            '1208', '1209', '1210', '1211', '1212', '1214', '1215', '1216', '1217', '1218',
            '1309', '1310', '1311', '1312', '1313', '1314', '1315', '1316', '1317', '1318',
            '1409', '1410', '1411', '1412', '1413', '1414', '1415', '1416', '1417',
            '1510', '1511', '1512', '1513', '1514', '1515', '1516', '1517',
            '1610', '1611', '1612', '1613', '1614', '1615', '1616',
            '1711', '1712', '1713', '1714', '1715', '1716'
        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_5_odd(self):
        '''Test 5-hex adjacency odd'''
        sector = Sector('Sector')
        radius = 5
        hex_id = '1120'
        nearby_hexes = [
            '0617', '0618', '0619', '0620', '0621', '0622',
            '0717', '0718', '0719', '0720', '0721', '0722', '0723',
            '0816', '0817', '0818', '0819', '0820', '0821', '0822', '0823',
            '0916', '0917', '0918', '0919', '0920', '0921', '0922', '0923', '0924',
            '1015', '1016', '1017', '1018', '1019', '1020', '1021', '1022', '1023', '1024',
            '1115', '1116', '1117', '1118', '1119', '1121', '1122', '1123', '1124', '1125',
            '1215', '1216', '1217', '1218', '1219', '1220', '1221', '1222', '1223', '1224',
            '1316', '1317', '1318', '1319', '1320', '1321', '1322', '1323', '1324',
            '1416', '1417', '1418', '1419', '1420', '1421', '1422', '1423',
            '1517', '1518', '1519', '1520', '1521', '1522', '1523',
            '1617', '1618', '1619', '1620', '1621', '1622'

        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_6_even(self):
        '''Test 6-hex adjacency even'''
        sector = Sector('Sector')
        radius = 6
        hex_id = '1213'
        nearby_hexes = [
            '0610', '0611', '0612', '0613', '0614', '0615', '0616',
            '0710', '0711', '0712', '0713', '0714', '0715', '0716', '0717',
            '0809', '0810', '0811', '0812', '0813', '0814', '0815', '0816', '0817',
            '0909', '0910', '0911', '0912', '0913', '0914', '0915', '0916', '0917', '0918',
            '1008', '1009', '1010', '1011', '1012',
            '1013', '1014', '1015', '1016', '1017', '1018',
            '1108', '1109', '1110', '1111', '1112',
            '1113', '1114', '1115', '1116', '1117', '1118', '1119',
            '1207', '1208', '1209', '1210', '1211',
            '1212', '1214', '1215', '1216', '1217', '1218', '1219',
            '1308', '1309', '1310', '1311', '1312',
            '1313', '1314', '1315', '1316', '1317', '1318', '1319',
            '1408', '1409', '1410', '1411', '1412', '1413', '1414', '1415', '1416', '1417', '1418',
            '1509', '1510', '1511', '1512', '1513', '1514', '1515', '1516', '1517', '1518',
            '1609', '1610', '1611', '1612', '1613', '1614', '1615', '1616', '1617',
            '1710', '1711', '1712', '1713', '1714', '1715', '1716', '1717',
            '1810', '1811', '1812', '1813', '1814', '1815', '1816'
        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

    def test_nearby_hex_6_odd(self):
        '''Test 6-hex adjacency odd'''
        sector = Sector('Sector')
        radius = 6
        hex_id = '1120'
        nearby_hexes = [
            '0517', '0518', '0519', '0520', '0521', '0522', '0523',
            '0616', '0617', '0618', '0619', '0620', '0621', '0622', '0623',
            '0716', '0717', '0718', '0719', '0720', '0721', '0722', '0723', '0724',
            '0815', '0816', '0817', '0818', '0819', '0820', '0821', '0822', '0823', '0824',
            '0915', '0916', '0917', '0918',
            '0919', '0920', '0921', '0922', '0923', '0924', '0925',
            '1014', '1015', '1016', '1017',
            '1018', '1019', '1020', '1021', '1022', '1023', '1024', '1025',
            '1114', '1115', '1116', '1117',
            '1118', '1119', '1121', '1122', '1123', '1124', '1125', '1126',
            '1214', '1215', '1216', '1217',
            '1218', '1219', '1220', '1221', '1222', '1223', '1224', '1225',
            '1315', '1316', '1317', '1318', '1319', '1320', '1321', '1322', '1323', '1324', '1325',
            '1415', '1416', '1417', '1418', '1419', '1420', '1421', '1422', '1423', '1424',
            '1516', '1517', '1518', '1519', '1520', '1521', '1522', '1523', '1524',
            '1616', '1617', '1618', '1619', '1620', '1621', '1622', '1623',
            '1717', '1718', '1719', '1720', '1721', '1722', '1723'

        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )


    def test_nearby_hex_corner_case(self):
        '''Test corner case adjacency'''
        sector = Sector('Sector')
        radius = 3
        hex_id = '0202'
        nearby_hexes = [
            '0101', '0102', '0103', '0104', '0105',
            '0201', '0203', '0204', '0205',
            '0301', '0302', '0303', '0304', '0305',
            '0401', '0402', '0403', '0404',
            '0501', '0502', '0503', '0504'

        ]
        print 'hex_id:', hex_id
        print 'actual:', set(nearby_hexes)
        print 'result:', set(sector.find_nearby_hexes(hex_id, radius))
        self.assertTrue(
            set(nearby_hexes) == set(sector.find_nearby_hexes(hex_id, radius))
        )

class TestIsEven(unittest.TestCase):
    '''Test _is_even method'''
    def test_is_even(self):
        '''Test _is_even returns True for even'''
        sector = Sector('sector')
        self.assertTrue(sector._is_even(2))

    def test_is_odd(self):
        '''Test _is_even returns False for odd'''
        sector = Sector('sector')
        self.assertFalse(sector._is_even(3))

class TestOwningSystemSubsector(unittest.TestCase):
    '''Test owning system'''
    def test_owning_system(self):
        '''Test owning system (subsector)'''
        # Subsector data - 0105 is the owned world, 0308 should be the owning world
        subsector = Subsector('Test sector')
        subsector.hexes = {}
        ss_data = [
            '{"mainworld": "{\\"trade_codes\\": [\\"Ni\\", \\"O:0101\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\":  \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"E9D8665-7\\",' + \
                '\\"orbit\\": 3,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 4,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 3,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 3,' + \
                '\\"spectral_type\\": \\"G\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"V\\"}",' + \
                '"Ix": "{-3}",' + \
                '"name": "Name-0105A",' + \
                '"zone": "",' + \
                '"Cx": "[5349]",' + \
                '"hex": "0105",' + \
                '"pbg": "202",' + \
                '"bases": "",' + \
                '"Ex": "(753+1)",' + \
                '"nobility": "B"}',
            '{"mainworld": "{\\"trade_codes\\": [\\"De\\", \\"Hi\\",' + \
                '\\"In\\", \\"Po\\", \\"Tz\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\":  \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"B140987-A\\",' + \
                '\\"orbit\\": 0,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 5,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 0,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 0,' + \
                '\\"spectral_type\\": \\"M\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"III\\"}",' + \
                '"Ix": "{+4}",' + \
                '"name": "Name-0308A",' + \
                '"zone": "",' + \
                '"Cx": "[ED17]",' + \
                '"hex": "0308",' + \
                '"pbg": "103",' + \
                '"bases": "",' + \
                '"Ex": "(A8A+1)",' + \
                '"nobility": "BEf"}',
            '{"mainworld": "{\\"trade_codes\\": [\\"Hi\\", \\"In\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\":  \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"A54598A-C\\",' + \
                '\\"orbit\\": 2,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 5,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 0,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 2,' + \
                '\\"spectral_type\\": \\"K\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"V\\"}",' + \
                '"Ix": "{+4}",' + \
                '"name": "Name-0805A",' + \
                '"zone": "",' + \
                '"Cx": "[5D4C]",' + \
                '"hex": "0805",' + \
                '"pbg": "403",' + \
                '"bases": "N",' + \
                '"Ex": "(98A+3)",' + \
                '"nobility": "BEf"}',
            '{"mainworld": "{\\"trade_codes\\": [\\"Ni\\", \\"Ag\\", \\"Pr\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\":  \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"B588510-8\\",' + \
                '\\"orbit\\": 3,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 9,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 7,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 3,' + \
                '\\"spectral_type\\": \\"G\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"V\\"}",' + \
                '"Ix": "{+0}",' + \
                '"name":' + \
                '"Name-0702A",' + \
                '"zone": "",' + \
                '"Cx": "[7567]",' + \
                '"hex": "0702",' + \
                '"pbg": "802",' + \
                '"bases": "",' + \
                '"Ex": "(B41-1)",' + \
                '"nobility": "BcC"}'
        ]
        for dta in ss_data:
            system = System()
            system.json_import(dta)
            subsector.hexes[system.hex] = system

        self.assertTrue(subsector.find_owning_system('0105') == '0308')
        subsector.trade_code_owning_system()
        self.assertTrue('O:0308' in subsector.hexes['0105'].mainworld.trade_codes)

        for _ in subsector.t5_tab():
            print _

class TestOwningSystemSector(unittest.TestCase):
    '''Test owning system'''
    def test_owning_system_sector(self):
        '''Test owning system (sector)'''
        # Sector data - 0105 is the owned world, 0308 should be the owning world
        sector = Sector('Test sector')
        sector.hexes = {}
        s_data = [
            '{"mainworld": "{\\"trade_codes\\": [\\"Ni\\", \\"O:0101\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\":  \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"E9D8665-7\\",' + \
                '\\"orbit\\": 3,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 4,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 3,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 3,' + \
                '\\"spectral_type\\": \\"G\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"V\\"}",' + \
                '"Ix": "{-3}",' + \
                '"name": "Name-0105A",' + \
                '"zone": "",' + \
                '"Cx": "[5349]",' + \
                '"hex": "0105",' + \
                '"pbg": "202",' + \
                '"bases": "",' + \
                '"Ex": "(753+1)",' + \
                '"nobility": "B"}',
            '{"mainworld": "{\\"trade_codes\\": [\\"De\\", \\"Hi\\",' + \
                '\\"In\\", \\"Po\\", \\"Tz\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\":  \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"B140987-A\\",' + \
                '\\"orbit\\": 0,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 5,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 0,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 0,' + \
                '\\"spectral_type\\": \\"M\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"III\\"}",' + \
                '"Ix": "{+4}",' + \
                '"name": "Name-0308A",' + \
                '"zone": "",' + \
                '"Cx": "[ED17]",' + \
                '"hex": "0308",' + \
                '"pbg": "103",' + \
                '"bases": "",' + \
                '"Ex": "(A8A+1)",' + \
                '"nobility": "BEf"}',
            '{"mainworld": "{\\"trade_codes\\": [\\"Hi\\", \\"In\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\": \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"A54598A-C\\",' + \
                '\\"orbit\\": 2,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 5,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 0,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 2,' + \
                '\\"spectral_type\\": \\"K\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"V\\"}",' + \
                '"Ix": "{+4}",' + \
                '"name": "Name-0805A",' + \
                '"zone": "",' + \
                '"Cx": "[5D4C]",' + \
                '"hex": "0805",' + \
                '"pbg": "403",' + \
                '"bases": "N",' + \
                '"Ex": "(98A+3)",' + \
                '"nobility": "BEf"}',
            '{"mainworld": "{\\"trade_codes\\": [\\"Ni\\", \\"Ag\\", \\"Pr\\"],' + \
                '\\"travel_code\\": \\"\\",' + \
                '\\"is_mainworld\\": true,' + \
                '\\"mainworld_type\\":  \\"Planet\\",' + \
                '\\"parent_type\\": null,' + \
                '\\"orbit_around_parent\\": null,' + \
                '\\"uwp\\": \\"B588510-8\\",' + \
                '\\"orbit\\": 3,' + \
                '\\"bases\\": \\"\\"}",' + \
                '"worlds": 9,' + \
                '"allegiance": "Na",' + \
                '"stellar": "{\\"decimal\\": 7,' + \
                '\\"companion\\": null,' + \
                '\\"habitable_zone\\": 3,' + \
                '\\"spectral_type\\": \\"G\\",' + \
                '\\"secondaries\\": {},' + \
                '\\"size\\": \\"V\\"}",' + \
                '"Ix": "{+0}",' + \
                '"name":' + \
                '"Name-0702A",' + \
                '"zone": "",' + \
                '"Cx": "[7567]",' + \
                '"hex": "0702",' + \
                '"pbg": "802",' + \
                '"bases": "",' + \
                '"Ex": "(B41-1)",' + \
                '"nobility": "BcC"}'
        ]
        for dta in s_data:
            system = System()
            system.json_import(dta)
            sector.hexes[system.hex] = system

        self.assertTrue(sector.find_owning_system('0105') == '0308')
        sector.trade_code_owning_system()
        self.assertTrue('O:0308' in sector.hexes['0105'].mainworld.trade_codes)

        for _ in sector.t5_tab():
            print _

class TestHexTransform(unittest.TestCase):
    '''Test transform between subsector hex and sector hex'''
    def test_subsectorhex_to_sectorhex(self):
        '''Test subsector hex to sector hex transform'''
        sctr = Sector('Sector')
        self.assertTrue(sctr.subsector_hex_to_sector_hex('0105', 'A') == '0105')
        self.assertTrue(sctr.subsector_hex_to_sector_hex('0105', 'B') == '0905')
        print sctr.subsector_hex_to_sector_hex('0810', 'A')
        self.assertTrue(sctr.subsector_hex_to_sector_hex('0810', 'A') == '0810')
        print sctr.subsector_hex_to_sector_hex('0810', 'B')
        self.assertTrue(sctr.subsector_hex_to_sector_hex('0810', 'B') == '1610')

    def test_sectorhex_to_subsectorhex(self):
        '''Test sector hex to subsector hex transform'''
        sctr = Sector('Sector')
        self.assertTrue(sctr.sector_hex_to_subsector_hex('0105') == '0105')
        self.assertTrue(sctr.sector_hex_to_subsector_hex('0905') == '0105')
        print 'Sector hex = {} subsector hex = {}'.format(
            '0810',
            sctr.sector_hex_to_subsector_hex('0810')
        )
        self.assertTrue(sctr.sector_hex_to_subsector_hex('0810') == '0810')
        print 'Sector hex = {} subsector hex = {}'.format(
            '0820',
            sctr.sector_hex_to_subsector_hex('0820')
        )
        self.assertTrue(sctr.sector_hex_to_subsector_hex('0820') == '0810')
    