"""
https://adventofcode.com/2021
"""
import utils
from utils import get_data


def day1():
    data = [int(x) for x in get_data(1)]
    results = {}

    # Part 1 - check how many elements n+1 > n
    results["part1"] = sum([data[i + 1] > data[i] for i in range(len(data) - 1)])

    # Part 2 - check how many elements sum(n, n+1, n+2) > sum(n+1, n+2, n+3)
    # elegant
    results["part2"] = sum([data[i + 3] > data[i] for i in range(len(data)-3)])

    # bruteforce
    '''
    triple_data = [sum([data[i + y] for y in range(3)]) for i in range(len(data) - 2)]
    results["part2"] = sum(
        [triple_data[i + 1] > triple_data[i] for i in range(0, len(triple_data) - 1)]
    )
    '''
  
    return results
    
def day2():
  data = [(str(a), int(b)) for a, b in [x.split() for x in get_data(2)]]
  results = {}

  # Part 1
  movement = {}
  for (k, v) in data: movement[k] = movement.get(k, 0) + int(v)
  results["part1"] = (movement["forward"]  * (movement["down"] - movement["up"]))

  # Part 2
  position, depth, aim = 0, 0, 0
  for dir, val in data:
    if dir == "down": aim += val
    elif dir == "up": aim -= val
    elif dir == "forward":
      position += val
      depth += (aim * val)
  results["part2"]  = position * depth

  return results

'''Today was experimenting with lambdas'''
def day3():
  pass
results = {}
  
split =            lambda x: [int(i) for i in x]
most_common_bit =  lambda x: int(sum(x) > len(x)/2)
binary2int =       lambda l: sum([(2*d)**i for i, d in enumerate(l[::-1])]) - (l[-1] == 0)

data = [split(x) for x in get_data(3)]
t_data = utils.transpose_list(data)
s_data = set(get_data(3))

# Part 1
gamma = [most_common_bit(i) for i in t_data]
epsilon = [int(not g) for g in gamma]
results["part1"] = binary2int(gamma) * binary2int(epsilon)

# Part 2
gamma_s = "".join(str(x) for x in gamma)
epsilon_s = "".join(str(x) for x in epsilon)

def build_combinations(stem:str, max_len:int):
  combinations = []
  if len(stem) == max_len:
    return [stem]
  else:
    for i in ["0", "1"]:
      combinations.extend(build_combinations(stem + i, max_len))
  return combinations


def get_rating(key:str):
  for i in range(len(key), 0, -1):
    substr = key[:i]
    if substr in s_data:
      o2_rating = substr
      return o2_rating
    else:
      # TODO fuzzy matching
      pass
  return None
  


#return results



if __name__ == "__main__":
  CURRENT_DAY = day3()
  print(CURRENT_DAY)