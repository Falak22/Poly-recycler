def game():
    return 1700098899


score = game()
with open('highscr.txt','r') as f:
    highscr=int(f.read())

if highscr<score :
    with open('highscr.txt','w') as f:
        f.write(str(score))
