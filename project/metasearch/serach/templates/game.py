def game_over():
    print("Game Over")
    exit()
def check_sides(left,right):
    if "ww1" in left and "wh1" not in left:
        game_over()
    if "ww2" in left and "wh2" not in left:
        game_over()
    if "ww1" in right and "wh1" not in right:
        game_over()
    if "ww2" in right and "wh2" not in right:
        game_over()
    if "bw" in left and "bh" not in left:
        game_over()
    if "bw" in right and "bh" not in right:
        game_over()
def select_pair(left,right):
    print("Enter the pair: ")
    pair = input().split()
    if pair[0][0] != pair[1][0]:
        game_over()
    left.remove(pair[0])
    left.remove(pair[1])
    right.append(pair[0])
    right.append(pair[1])
    check_sides(left,right)
    print(str(left)+" <--> "+str(right))
    return (left,right)
def select_return(left,right):
    print("Enter the returnee: ")
    re = input()
    right.remove(re)
    left.append(re)
    check_sides(left,right)
    print(str(left)+" <--> "+str(right))
    return (left,right)
def fn():
    left = ["wh1","ww1","wh2","ww2","bh","bw"]
    right = []
    print(str(left)+" <--> "+str(right))
    while len(left) != 0:
        (left,right) = select_pair(left,right)
        (left,right) = select_return(left,right)
    print("You Won")
fn()