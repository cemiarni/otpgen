"""One-time password generator.

Usage:
    otpgen list
    otpgen <profile>
    otpgen add <profile> <secret>
    otpgen modify <profile> <secret>
    otpgen rename <profile> <new_profile>
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
    list      Lists all available profiles.
    add       Adds new profile with a given secret.
    modify    Modifies the secret of the given profile.
    rename    Renames a given profile.
    remove    Removes the given profile.

"""


import pyotp
import os
import sys
from docopt import docopt


OTP_DIR = os.path.join(os.path.expanduser('~'), '.otp')


def main():
    args = docopt(__doc__, version="otpgen 1.2")
    if args["<profile>"]:
        profile_path = os.path.join(OTP_DIR, args["<profile>"])
    else:
        profile_path = None

    if args["add"] or args["modify"]:
        if not os.path.exists(OTP_DIR):
            os.makedirs(OTP_DIR)
        with open(profile_path, 'w') as f:
            f.write(args["<secret>"])
    elif args["remove"]:
        if os.path.exists(profile_path):
            os.remove(profile_path)
    elif args["rename"]:
        if os.path.exists(profile_path):
            os.rename(profile_path,
                      os.path.join(OTP_DIR, args["<new_profile>"]))
        else:
            print("The %s profile does not exist!" % args["<profile>"])
    elif args["list"]:
        for profile in os.listdir(OTP_DIR):
            print(profile)
    else:
        if os.path.exists(profile_path):
            with open(profile_path) as f:
                secret = f.read()
            totp = pyotp.TOTP(secret)
            print(totp.now())
        else:
            print("The %s profile does not exist!" % args["<profile>"])


if __name__ == "__main__":
    sys.exit(main())
