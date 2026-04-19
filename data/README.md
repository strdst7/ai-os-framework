# Dataset Notes

This folder contains lightweight synthetic telemetry used for demonstrating AI-OS Framework scoring and evaluation.

These datasets are illustrative and reproducible.

Files:

- sample_telemetry.csv
- synthetic_incidents.csv

import pandas as pd

df = pd.read_csv("data/sample_telemetry.csv")
print(df.head())
