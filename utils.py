from unittest import TestCase

class Test_PA(TestCase):
    def test(self, find_peaks):
        self.assertEqual(find_peaks([1,2,3,6,4,1,2,3,2,1]), {"pos": [3,7], "peaks": [6,3]})
        self.assertEqual(find_peaks([3,2,3,6,4,1,2,3,2,1,2,3]), {"pos": [3,7], "peaks": [6,3]})
        self.assertEqual(find_peaks([3,2,3,6,4,1,2,3,2,1,2,2,2,1]), {"pos": [3,7,10], "peaks": [6,3,2]})
        self.assertEqual(find_peaks([2,1,3,1,2,2,2,2,1]), {"pos": [2,4], "peaks": [3,2]})
        self.assertEqual(find_peaks([2,1,3,1,2,2,2,2]), {"pos": [2], "peaks": [3]})
        self.assertEqual(find_peaks([2,1,3,2,2,2,2,5,6]), {"pos": [2], "peaks": [3]})
        self.assertEqual(find_peaks([2,1,3,2,2,2,2,1]), {"pos": [2], "peaks": [3]})
        self.assertEqual(find_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]), {"pos": [2,7,14,20], "peaks": [5,6,5,5]})
        self.assertEqual(find_peaks([-3,10,9,18,8,-4,-5,4,12,1,15,-5,10,2,18,3,5,12,12]), {"pos": [1,3,8,10,12,14], "peaks": [10,18,12,15,10,18]})
        self.assertEqual(find_peaks([15,19,18,-2,3,6,19,20,-4,19,-5,-5,-3,8,18,15,-4,-1,14]), {"pos": [1,7,9,14], "peaks": [19, 20, 19, 18]})
        self.assertEqual(find_peaks([]), {"pos": [], "peaks": []})
        self.assertEqual(find_peaks([1,1,1,1]), {"pos": [], "peaks": []})
        print("Test OK")
