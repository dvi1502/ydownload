import unittest

from ydownload.__main__ import *


class Test(unittest.TestCase):
    def test_clean_folder(self):
        directory_path = "/home/dvi/downloads/py/python3-spock"
        for filename in os.listdir(directory_path):
            if filename.endswith('mp4'):
                base_name, _ = os.path.splitext(filename)
                file_path = os.path.join(directory_path, base_name + '.wav')
                with open(file_path, 'a') as f:
                    pass
                    print(f"Empty file '{file_path}' created.")

        clean_folder(directory_path, 'wav')


if __name__ == '__main__':
    unittest.main
