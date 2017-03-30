from setuptools import setup, find_packages
setup(
    name="otpgen",
    version="1.0",
    packages=find_packages(),
    install_requires=['pyotp'],
    entry_points={'console_scripts': ['otpgen = otpgen:main']}
)
