from setuptools import setup, find_packages

setup(
    name = 'dcommit',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/dcommit.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'dcommit is a git committer that can specify commit date.',
    install_requires = ['setuptools', "argparse", "GitPython"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "dcommit = dcommit.dcommit:main",
        ]
    }
)
