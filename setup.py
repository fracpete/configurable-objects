from setuptools import setup


def _read(f):
    """
    Reads in the content of the file.
    :param f: the file to read
    :type f: str
    :return: the content
    :rtype: str
    """
    return open(f, 'rb').read()


setup(
    name="configurable_objects",
    description="Library for making it easy to manage parameters of objects via dictionaries or JSON.",
    long_description=(
        _read('DESCRIPTION.rst') + b'\n' +
        _read('CHANGES.rst')).decode('utf-8'),
    url="https://github.com/fracpete/configurable-objects",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    package_dir={
        '': 'src'
    },
    packages=[
        "confobj",
    ],
    version="0.0.1",
    author='Peter "fracpete" Reutemann',
    author_email='configurable-objects@fracpete.org',
)
