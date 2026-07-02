import argparse

# Will parse automatically the args
parser = argparse.ArgumentParser(prog="Media Compressor", description="Compress image and videos", epilog="By vitozap")
parser.add_argument("-v", "--verbose",   help="Displays more info about...")
args = parser.parse_args()
print(args)

