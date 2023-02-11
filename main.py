import pandas as pd

def main():
    print(f'{pd.__version__=}')
    df = pd.DataFrame(['Hello World'], columns=['message'])
    print(df)
    return None

if __name__=="__main__":
    main()