'''
Draws the stick man based on how many guesses are remaining

    O
   /|\
   / \

'''
def draw_stick(guesses_remaining):
    head = 'O' if guesses_remaining <= 5 else ' '
    body = '|' if guesses_remaining <= 4 else ' '
    l_arm = '/' if guesses_remaining <= 3 else ' '
    r_arm = '\\' if guesses_remaining <= 2 else ' '
    l_leg = '/' if guesses_remaining <= 1 else ' '
    r_leg = '\\' if guesses_remaining == 0 else ' '
    print('\n%s' % head.center(9))
    print((l_arm + body + r_arm).center(9))
    print('%s\n' % ' '.join([l_leg, r_leg]).center(9))
