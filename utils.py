def get_data(day: int):
    with open(f"./data/day{day}.txt", "r") as df:
        data = [x.strip() for x in df.readlines()]
    return data

# TODO do this with zip
def transpose_list(l:list):
  tlist = []
  for i in range(len(l[0])):
    tlist.append([x[i] for x in l])
  return tlist