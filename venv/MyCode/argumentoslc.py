__author__ = "Fabrício L. Ribeiro"


import argparse as ap


def main():
    p = ap.ArgumentParser(description="Jogue um jogo-da-velha")
    grp = p.add_mutually_exclusive_group()
    grp.add_argument("-n", "--new", action='store_true', help="start new game")
    grp.add_argument("-r", "--res", "--restore",
                     action='store_true', help="restore old game")
    grp2 = p.add_mutually_exclusive_group()
    grp2.add_argument("-a", "--ant", action='store_true',
                      help="Testa anterior")
    grp2.add_argument("-b", "--buzz", action='store_true', help="Faz um buzz")
    args = p.parse_args()

    if args.new:
        executeChoice(1)
    elif args.res:
        executeChoice(2)
    else:
        while True:
            choice = getMenuChoice(menu)
            executeChoice(choice)


if __name__ == "__main__":
    main()
