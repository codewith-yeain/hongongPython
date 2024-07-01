def hanoiTop(count, start, end, sub):
    if count == 1:
        print("{}탑 -> {}탑".format(start, end))
    if count >= 2:
        temp = count-1
        hanoiTop(count-1, start, end, sub)
        hanoiTop(temp-1, start, end, sub)

hanoiTop(4, "A", "B", "C")