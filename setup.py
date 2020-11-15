from setuptools import setup,  find_packages

with open("README.rst", encoding="UTF-8") as f:
	readme=f.read()

setup(
	name='pgbackup',
	version='0.1.0',
	description='Database backups locally',
	long_description=readme,
	author='LaShondra',
	author_email='tolliverl1@nku.edu',
	packages=find_packages('src'),
	package_dir={'':'src'},
	install_requires=[]
)
