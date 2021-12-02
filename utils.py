def get_data(day: int):
    with open(f"./data/day{day}.txt", "r") as df:
        data = [x.strip() for x in df.readlines()]
    return data
