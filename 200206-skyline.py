def generate_skyline(buildings):
  # Fill this in.
  # check overlap with previous building 
  #   if(prev[right] > now[left]):
  #     prev[right] = now[left] - 1
  #   if(prev[right] > now[right]):
  #     buildings.append((now[right]+1, prev[right], prev[height]))
  iterator = 0
  while iterator < len(buildings):
    now = buildings[iterator]
    if(iterator != 0):
      prev = buildings[iterator-1]
      if(prev[1] > now[0]):
        newPrev = (prev[0], now[0] - 1, prev[2])
        buildings[iterator-1] = newPrev
      if(prev[1] > now[1]):
        buildings.append((now[1]+1, prev[1], prev[2]))
    iterator += 1
  result = []
  right = 0
  for building in buildings:
    start = building[0]
    right = building[1]
    height = building[2]
    result.append((start, height))
  if (right < 9):
    result.append((right+1, 0))
  return result

#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]