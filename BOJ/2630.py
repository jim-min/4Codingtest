import sys

n = int(sys.stdin.readline())
paper = []
white_paper_count = 0
blue_paper_count = 0

for _ in range(n):
    li = sys.stdin.readline().split()
    paper.append(li)

# 한 함수에서 한 번에 하는 방법을 찾으려고 했는데 return 값이 3개 나오고 난리나서 걍 함수 두 개 만듦
def cut_blue(n, x, y):
    global blue_paper_count
    if n == 1:
        if paper[x][y] == '1':
            return True
        
        else:
            return False
    
    one = cut_blue(n//2, x, y)
    two = cut_blue(n//2, x+n//2, y)
    three = cut_blue(n//2, x, y+n//2)
    four = cut_blue(n//2, x+n//2, y+n//2)

    if (one and two and three and four):
        return True
    
    else:
        for i in [one, two, three, four]:
            if i:
                blue_paper_count += 1

        return False
    
def cut_white(n, x, y):
    global white_paper_count
    if n == 1:
        if paper[x][y] == '0':
            return True
        
        else:
            return False
    
    one = cut_white(n//2, x, y)
    two = cut_white(n//2, x+n//2, y)
    three = cut_white(n//2, x, y+n//2)
    four = cut_white(n//2, x+n//2, y+n//2)

    if (one and two and three and four):
        return True
    
    else:
        for i in [one, two, three, four]:
            if i:
                white_paper_count += 1

        return False
    
blu = cut_blue(n, 0, 0)
wit = cut_white(n, 0, 0)

if blu:
    blue_paper_count += 1

if wit:
    white_paper_count += 1

print(white_paper_count)
print(blue_paper_count)

