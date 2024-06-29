grocery = {}

while True:
    try:
        name = input().upper()
        if name in grocery:
            grocery[name] += 1
        else:
            grocery[name] = 1
    except (EOFError, KeyboardInterrupt):
        for i in sorted(grocery.keys()):
            print(grocery[i], i.upper())
        break
        
