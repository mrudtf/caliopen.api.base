import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'caliopen.base.user',
    'pyramid',
    'zope.interface',
    'cornice',
    'colander',
    ]

extras_require = {
    'dev': [],
    'test': [],
}

setup(name='caliopen.api.base',
      namespace_packages=['caliopen', 'caliopen.api'],
      version='0.0.1',
      description='Caliopen base REST API package.',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
                  "Programming Language :: Python",
                  "Framework :: Pyramid"],
      author='Caliopen Contributors',
      author_email='contact@caliopen.org',
      url='https://caliopen.org',
      license='AGPLv3',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require=extras_require,
      install_requires=requires,
      tests_require=requires,
      )
