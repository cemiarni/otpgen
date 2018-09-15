# otpgen
Command line one-time password generator

# Usage
```
$ otpgen --help
One-time password generator.

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
```
