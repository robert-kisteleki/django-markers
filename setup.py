import os
from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES

app_name = 'crocodile'
version = __import__(app_name).__version__

# Tell distutils to put the data_files in platform-specific installation
# locations. See here for an explanation:
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk(app_name):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len(app_name)+1:] # Strip "app_name/" or "app_name\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='django-' + app_name,
    version=version,
    description="A dynamic map marker generator for your Django site.",
    long_description=open('README.md').read(),
    author='Daniel Quinn',
    author_email='me@danielquinn.org',
    url="https://github.com/danielquinn/django-markers",
    package_dir={app_name: app_name},
    packages=packages,
    package_data={app_name: data_files},
    install_requires=["PIL",],
    classifiers=[
        'Development Status :: 5 - Production/Unstable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: GPL-3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
    zip_safe=False,
)

