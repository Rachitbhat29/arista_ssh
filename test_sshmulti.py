import unittest
import utils

class MyTestCase(unittest.TestCase):

    # setup will run first
    def setUp(self):
        pass

    def test_parsehost_hostname_w_port(self):
        host = 'localhost:123'
        res = utils.parseHost(host)
        self.assertEqual(len(res), 4)
        self.assertEqual(res[0], 'localhost')
        self.assertEqual(res[2], 'bhumikasanghvi')
        self.assertEqual(res[3], '242919')

    def test_parsehost_hostname_only(self):
        host = 'localhost'
        res = utils.parseHost(host)
        self.assertEqual(res[1], 22)
        self.assertEqual(res[0], 'localhost')
        self.assertEqual(res[2], 'bhumikasanghvi')
        self.assertEqual(res[3], '242919')

    def test_parsehost_hostname_w_port_userpass(self):
        host = 'localhost:22 bhumikasanghvi@242919'
        res = utils.parseHost(host)
        self.assertEqual(res[1], 22)
        self.assertEqual(res[0], 'localhost')
        self.assertEqual(res[2], 'bhumikasanghvi')
        self.assertEqual(res[3], '242919')

    def test_getCpuCores(self):
        host = 'localhost:22 bhumikasanghvi@242919'
        client = utils.connectSSH(host,)[1]
        output = utils.getCpuCores(client)
        self.assertEqual(output, 4)

    #this will run after the test cases
    def tearDown(self):
        #your code to clean or close the connection
        pass

if __name__ == '__main__':
    unittest.main()
