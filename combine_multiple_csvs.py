import pandas as pd
import glob
import pathlib

path = pathlib.Path().absolute() / "csv_files"


def combine(path, name="combined"):
    all_csvs = glob.glob(str(path) + "/*.csv")
    df = pd.concat((pd.read_csv(f) for f in all_csvs), ignore_index=True)
    return df.to_csv(f"{name}.csv", index=False)


combine(path)
