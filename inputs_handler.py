import argparse


def createparser():
    parser = argparse.ArgumentParser()
    parser.add_argument('link', help='Ссылка')

    return parser
