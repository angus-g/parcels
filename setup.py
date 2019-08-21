"""Install Parcels and dependencies."""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(name='parcels',
      description="""Framework for Lagrangian tracking of virtual
      ocean particles in the petascale age.""",
      author="oceanparcels.org team",
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      packages=find_packages(),
      install_requires=[
          'cgen',
          'numpy',
          'progressbar2',
          'pymbolic',
          'scipy',
          'six',
          'xarray',
          'cftime',
          'netCDF4',
          'dask[array]',
          'psutil'],
      package_data={'parcels': ['include/*',
                                'examples/*']},
      entry_points={'console_scripts': [
          'parcels_get_examples = parcels.scripts.get_examples:main']}
      )
