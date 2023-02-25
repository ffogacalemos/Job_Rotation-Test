def revstring():
    s = "abcdefghijklmnopqrstuvwxyz"

    for i in range(len(s)-1, -1, -1):
        print(f"{s[i]}", end='')
