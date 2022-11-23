filename = input("파일 이름을 입력하세오: ")
infile = open(filename,"r")
read_file = infile.readlines()

outfile = open(filename, "w")
del_word = input("삭제할 문자열을 입력하시오: ")

for line in read_file:
    l, r = 0, len(del_word)
    new_line = "" 
    while l < len(line):
        if line[l:r] == del_word:
            l += len(del_word)
            r += len(del_word)
        else:
            new_line += line[l]
            l+=1
            r+=1
    print(new_line, file = outfile, end="")

infile.close()
outfile.close()
print("변경된 파일이 저장되었습니다.")