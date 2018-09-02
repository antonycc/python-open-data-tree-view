#!/usr/bin/env python3
# Purpose: Unit tests for Tree View
# Usage:
#    source venv/bin/activate
#    python3 -m unittest discover .

import os
from pathlib import Path
import pandas as pd
import unittest

import config
import persistence

# Config
logger = config.get_logger()

# Constants
source_filepath = Path('./examples/My building.csv')
output_path = './tmp'
floor_height_label = 'floor_height'
face_direction_label = 'face_direction'
window_vertical_position_label = 'window_vertical_position'


# Data builders
def load_dataframe():
    df = pd.read_csv(filepath_or_buffer=str(source_filepath))
    return df


# Tests
class TestAggregation(unittest.TestCase):

    def setUp(self):
        logger.debug("Set-up")
        if not os.path.exists(output_path):
            os.makedirs(output_path)

    def tearDown(self):
        logger.debug("Tear-down")

    def test_to_logging(self):
        df = load_dataframe()
        assert len(df)
        persistence.to_logging(df,
                          floor_height_column=floor_height_label,
                          face_direction_column=face_direction_label,
                          window_vertical_position_column=window_vertical_position_label)

    def test_to_persistence(self):
        df = load_dataframe()
        assert len(df) > 0
        # assert output_filepath.exists()

    def test_to_persistence_with_list(self):
        df = load_dataframe()
        assert len(df) > 0
        # assert output_filepath.exists()


if __name__ == '__main__':
    unittest.main()
