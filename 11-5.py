a = input("입력 파일 이름: ")
b = input("출력 파일 이름: ")


infile = open(a, "r")
outfile = open(b, "w")


t = 0.0
c = 0


line = infile.readline()
while line != "" :
  k = float(line)
  t = t + k
  c = c + 1
line = infile.readline()


outfile.write("합계="+ str(t)+"\n")


avg = t / c
outfile.write("평균="+ str(avg)+"\n")


infile.close()
outfile.close()