from os.path import expanduser
import argparse
import pyotp
import os
import sys


OTP_DIR = os.path.join(expanduser('~'), '.otp')

parser = argparse.ArgumentParser()

parser.add_argument('profile', metavar='PROFILE', type=str, nargs=1)
parser.add_argument('--create', metavar='SECRET', type=str)
parser.add_argument('--rm', action='store_true')


def main():
    args = parser.parse_args()
    profile_path = os.path.join(OTP_DIR, args.profile[0])
    if args.create:
        if not os.path.exists(OTP_DIR):
            os.makedirs(OTP_DIR)
        with open(profile_path, 'w') as f:
            f.write(args.create)
    elif args.rm:
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
