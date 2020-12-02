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
	#you can edit the following line with the new install_requires boto3 entry
	install_requires=['boto3'],
	entry_points={
	'console_scripts':[
		'pgbackup=pgbackup.cli:main'
	]
}
	#you need to define your entry point as a setup function parameter
)

# the following two lines should be required as parameters of setup function. You can replace the current install_required[] with the new one in your setup function
# install_requires=['boto3']

