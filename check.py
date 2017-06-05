import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo1")
parser.add_argument("echo2")
args = parser.parse_args()
print(args.echo1)
print(arg.echo2)
