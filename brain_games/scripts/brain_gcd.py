#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games import game_engine


def main():
    game_engine.play(gcd)


if __name__ == '__main__':
    main()
