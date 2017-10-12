with open("test.txt") as f:
  while c:
    c = f.read(1)
    if not c:
      print("End of file")
      break
    print("Read a character:", c)