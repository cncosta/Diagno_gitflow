import pandas as pd


def open_file():
    raw_data = pd.read_json("farmers-protest-tweets-2021-03-5.json", lines=True)
    data = pd.DataFrame(raw_data)
    return data


def top_retweet(df):
    topten_rt = df.nlargest(10, "retweetCount")
    print(topten_rt.loc[:, ["content", "retweetCount"]])
    return


def main():
    """
    this is the main function
    """
    data = open_file()
    print("Los top 10 tweets más retweeted.")
    top_retweet(data)
    return


if __name__ == "__main__":
    main()
