with open('a_an_example.in.txt',"r") as record:
  clients = True
  LikeList, DislikeList = [], []
  is_dlike = 0
  for rec in record:
    # below client condition is used to ignore first line in records
    if clients:
      clients = False
      continue
    # is_dlike local varaible is used to filter Like and Dislike record lines from file 
    if is_dlike == 0:
      splits = rec[2:].split()
      for i in splits:
        LikeList.append(i)
      is_dlike = 1
    else:
      splits = rec[2:].split()
      for i in splits:
        DislikeList.append(i)
      is_dlike = 0
  if DislikeList:
    FinalList = list(set(LikeList).difference(DislikeList))
    print(len(FinalList), ' '.join(map(str, set(FinalList))))
  else:
    print(len(set(LikeList)), ' '.join(map(str, set(LikeList))))
