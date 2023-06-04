from distutils.core import setup


VERSION = '0.0.1'


def read_file(path):
    with open(path) as f:
        return f.read()


setup(
    name='feed2exec_extensions',
    version=VERSION,
    description='My collections of [feed2exec](https://github.com/dbiesecke/feed2exec) plugins.',
    log_descrption=read_file('README.rst'),
    author='Ryosuke Ito',
    author_email='rito.0305@gmail.com',
    url='https://github.com/manicmaniac/feed2exec_extensions',
    packages=['feed2exec_extensions'],
    keywords=[
        'feed2exec',
        'plugin',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ]
)
