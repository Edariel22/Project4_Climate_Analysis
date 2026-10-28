"""Targeted checks of baseline and coverage correctness, using synthetic fixtures."""
import unittest
import pandas as pd
from src.project_setup import annual_anomalies, coverage

class SetupChecks(unittest.TestCase):
    def test_baseline_and_incomplete_year(self):
        dates = pd.date_range('1951-01-01', '1981-11-01', freq='MS')
        frame = pd.DataFrame({'dt': dates, 'LandAndOceanAverageTemperature': 10.0})
        result = annual_anomalies(frame)
        self.assertTrue((result.loc['1951':'1980', 'anomaly'] == 0).all())
        self.assertTrue(pd.isna(result.loc['1981-01-01', 'mean']))

    def test_incomplete_reference_period_rejected(self):
        frame = pd.DataFrame({'dt': pd.date_range('1951-01-01', '1979-12-01', freq='MS'),
                              'LandAndOceanAverageTemperature': 10.0})
        with self.assertRaises(ValueError):
            annual_anomalies(frame)

    def test_locations_not_row_count(self):
        frame = pd.DataFrame({'date': ['2000-01-01', '2000-01-02', '2000-01-02'],
                              'location': ['A', 'A', 'B'], 'value': [1, None, 3]})
        result = coverage(frame, 'date', 'location')
        self.assertEqual(result['locations'], 2)
        self.assertEqual(result['missing_cells'], 1)

if __name__ == '__main__':
    unittest.main()
