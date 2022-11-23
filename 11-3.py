filename = input("입력 파일 이름: ").strip()
infile = open(filename, "r")


def func(line, counter):
  for c in line:
    if c.isalpha():
      if c in counter:
       counter[c] = counter[c] + 1
  else:
    counter[c] = 1


dic = { }
for line in infile:
  func(line, dic)
print(dic)
infile.close()