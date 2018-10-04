# -*- coding: utf-8 -*-
__author__ = "Negro"

import sys
import unittest

import connection


class Testconnection(unittest.TestCase):

   

    def test_statuscode(self):
        URL="http://www.marca.com/"
        a=connection.statuscode(URL)
        self.assertEqual(a,200)
    
    def test_getwithoutAuth(self):
        URL="http://www.marca.com/"
        a=connection.getwithoutAuth(URL)
        self.assertIsNotNone(a)



if __name__ == "__main__":
    unittest.main()
