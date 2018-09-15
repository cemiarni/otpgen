from setuptools import setup
setup(
    name="otpgen",
    version="1.1",
    py_modules=['otpgen'],
    install_requires=['pyotp', 'docopt'],
    entry_points={'console_scripts': ['otpgen = otpgen:main']}
)
