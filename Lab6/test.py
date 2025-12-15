import unittest
from main import Polygon

class TestPolygonPos(unittest.TestCase):

    def setUp(self):
        self.polygon = Polygon([(0,0), (4,0), (4,4), (0,4)])
        self.test_cases = [
            {"desc": "внутри",       "point": (2,2), "expected": "1"},
            {"desc": "снаружи",      "point": (5,5), "expected": "-1"},
            {"desc": "на стороне",    "point": (0,2), "expected": "0"},
            {"desc": "на вершине",   "point": (0,0), "expected": "0"},
            {"desc": "вне по общему случаю", "point": (-1,-1), "expected": "-1"},
        ]

    def test_point_pos(self):
        for case in self.test_cases:
            with self.subTest(case=case["desc"]):
                result = self.polygon.point_pos(case["point"])
                self.assertEqual(result, case["expected"], f"Failed for {case['desc']}")

if __name__ == "__main__":
    unittest.main()
    
