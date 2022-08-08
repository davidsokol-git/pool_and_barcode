import pandas as pd

# CHANGEME: point file path to the csv file obtained from Illumina's pooling calculator
input = "~/Documents/code/git_hub/pool_and_barcode/example/illumina_calc_results_example.csv"

# CHANGEME: point file path to the directory containing experimental data
output = "~/Documents/code/git_hub/pool_and_barcode/example/barcode_csv_example.csv"

pool_calc_df = pd.read_csv(input, header = 24)
pool_calc_df.rename(columns = {"Unnamed: 0": "well"}, inplace = True)
pool_calc_df = pool_calc_df[2:-2]

barcode_df = "~/Documents/code/git_hub/pool_and_barcode/scwgbs_barcode_v4.csv"
barcode_df = pd.read_csv(barcode_df)

pool_barcode_df = pd.merge(pool_calc_df, barcode_df, on = "well")

data = [pool_barcode_df["well"], pool_barcode_df["name"], pool_barcode_df["barcode_1"], pool_barcode_df["barcode_2"]]
headers = ["sample", "barcode_name", "barcode_1", "barcode_2"]
barcode_csv = pd.concat(data, axis=1, keys=headers)
barcode_csv.to_csv(output, index=False)
