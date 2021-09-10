from argparse import ArgumentParser


def run(url):
    pass


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-nc', '--n-commits', dest='n_commits', default=10,
                        help='show n last commits (default: shows 10 last commits)')
    args = parser.parse_args()
    while True:
        run(input('\nInput github url: \t\t\t\t\t\t\t\t (type exit() to close program)\n\t').lower())
