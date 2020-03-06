####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'DA'
strategy_name = 'Math time'
strategy_description = """"\
If they betrayed in the last four rounds, betray,
If in the last 6 rounds they colluded betray,
If we colluded in the last three rounds betray,
Math to decide twice,
When in doubt, betray
"""

import random


def move(my_history, their_history, my_score, their_score, opponent_name):
    """Make my move based on the history with this player.

    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty.
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]

    Returns 'c' or 'b' for collude or betray.
    """

    if len(their_history) >= 4:
        if 'b' in their_history[-4]:  # If the other player has betrayed within last 4 rounds,
            return 'b'  # Betray
        else:
            if len(their_history) >= 6:
                if 'b' not in their_history[-6]:  # If other player has colluded past 4 rounds
                    return 'b'  # Betray
            else:
                if len(my_history) >= 4:
                    if 'c' in my_history[-3]:  # If we colluded the past three times
                        return 'b'  # Betray
                else:
                    if my_score >= their_score + 2 * their_score:  # math
                        return 'c'  # collude
                    else:
                        if their_score >= my_score + 2 * their_score:  # math
                            return 'b'  # betray
                        else:
                            if len(their_history) >= 2:
                                if 'b' not in their_history[-2]:
                                    return 'c'  # collude
                            else:
                                if 'b' not in their_history[-2]:
                                    return 'c'  # collude
                                else:
                                    return 'b' and print("Death Before Surrender!")

    else:
        if my_score >= their_score + 2 * their_score:  # math
            return 'c'  # collude
        else:
            if their_score >= my_score + 2 * their_score:  # math
                return 'b'  # betray
            else:
                if their_history >= 2:
                    if 'b' not in their_history[-2]:
                        return 'c'  # collude
                else:
                    if 'b' not in their_history[-2]:
                        return 'c'  # collude
                    else:
                        return 'b' and print("Death Before Surrender!")