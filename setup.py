import codecs
from setuptools import setup, find_packages

setup(name='pyJasper',
      maintainer='Marcel Portela',
      maintainer_email='marcel.portela@gmail.com',
      url='https://github.com/mportela/pyJasper',
      version='6.0.0',
      description='toolkit to access JasperReports from Python',
      long_description=codecs.open('README.markdown', "r", "utf-8").read(),
      license='BSD',
      classifiers=['Intended Audience :: Developers',
                   'Programming Language :: Python'],
      
      packages = find_packages(),
      package_data = {
          # If any package contains *.txt or *.rst files, include them:
          '': ['*.xml', '*.jrxml', '*.jar', '*.py', '*.sh'],
          #backend/lib/
          #backend/webapps/
      },
      install_requires = ['httplib2'],
      zip_safe = False,
)
