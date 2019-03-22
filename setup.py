#!/usr/bin/env python
"""chaostoolkit-service-fabric extension builder and installer"""

import sys
import io

import setuptools

sys.path.insert(0, ".")
from chaosservicefabric import __version__
sys.path.remove(".")

name = 'chaostoolkit-service-fabric'
desc = 'Chaos Toolkit Extension for Microsoft Service Fabric'

with io.open('README.md', encoding='utf-8') as strm:
    long_desc = strm.read()


packages = [
    'chaosservicefabric',
    'chaosazure.fabric'
]

needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []

test_require = []
with io.open('requirements-dev.txt') as f:
    test_require = [l.strip() for l in f if not l.startswith('#')]

install_require = []
with io.open('requirements.txt') as f:
    install_require = [l.strip() for l in f if not l.startswith('#')]

setup_params = dict(
    name=name,
    version=__version__,
    description=desc,
    long_description=long_desc,
    long_description_content_type='text/markdown',
    classifiers=classifiers,
    author=author,
    author_email=author_email,
    url=url,
    license=license,
    packages=packages,
    include_package_data=True,
    install_requires=install_require,
    tests_require=test_require,
    setup_requires=pytest_runner,
    python_requires='>=3.5.*'
)


def main():
    """Package installation entry point."""
    setuptools.setup(**setup_params)


if __name__ == '__main__':
    main()
