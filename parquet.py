from tkinter.filedialog import askopenfilename
import pandas as pd

if __name__ == "__main__":
    filename = askopenfilename()
    print(filename)
    df = pd.read_parquet(filename)
    df.to_csv(filename + '.csv')