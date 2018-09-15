"""One-time password generator.

Usage:
    otpgen <profile>
    otpgen add <profile> <secret>
    otpgen modify <profile> <secret>
    otpgen remove <profile>
    otpgen (-h | --help)
    otpgen --version

Options:
    -h --help   Show this screen.
    --version   Show version

The program requires a profile name (<profile>) or a command.
After a profile was given, the program generates
a one-time password, that uses the profile's secret.
You can also give an other command, from below:
    add       Adds new profile with a given secret.
    modify    Modifies the secret of the given profile.
    remove    Removes the given profile.

"""

from docopt import docopt
from os.path import expanduser
import pyotp
import os
import sys


OTP_DIR = os.path.join(expanduser('~'), '.otp')


def main():
    args = docopt(__doc__, version="otpgen 1.1")
    profile_path = os.path.join(OTP_DIR, args["<profile>"])
    if args["add"] or args["modify"]:
        if not os.path.exists(OTP_DIR):
            os.makedirs(OTP_DIR)
        with open(profile_path, 'w') as f:
            f.write(args["<secret>"])
    elif args["remove"]:
        if os.path.exists(profile_path):
            os.remove(profile_path)
    else:
        if os.path.exists(profile_path):
            with open(profile_path) as f:
                secret = f.read()
            totp = pyotp.TOTP(secret)
            print(totp.now())


if __name__ == "__main__":
    sys.exit(main())
