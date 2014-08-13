# unzipper.py - A small program created in python that can crack a zip file.
# The zip file's password must contain a simple word only.
# We try each word contained in 'dictionary.txt'.

# Raymond Ho
# August 12, 2014

import sys, zipfile

def extract(zFile, password):

    try:
        zFile.extractall(pwd = password)
        return password
    except:
        pass

def main():

    if len(sys.argv) is not 2:
        sys.exit("USE: python unzipper.py [zipped file/folder]")

    zFile = zipfile.ZipFile(sys.argv[1])

    List = []
    with open('dictionary.txt', 'r') as f:
        List = f.read().splitlines()

    print 'Hacking away..'

    for password in List:

        guess = extract(zFile, password)
        if guess:
            print 'Password for %s: "%s"' % (sys.argv[1], password)
            exit(0)

    else:
            print 'No password found.'


if __name__ == "__main__":
    main()
