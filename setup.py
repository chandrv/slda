from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import cython_gsl

extensions = [
    Extension('lda_cython._topic_models', ['lda_cython/_topic_models.pyx'],
              libraries=cython_gsl.get_libraries(),
              library_dirs=[cython_gsl.get_library_dir()],
              include_dirs=[numpy.get_include(), cython_gsl.get_include()]),
    Extension('pypolyagamma.pypolyagamma', ['pypolyagamma/pypolyagamma.pyx'],
              include_dirs=[numpy.get_include(), 'pypolyagamma/pypolyagamma/cpp/include',]),
]

setup(
    name='lda-cython',
    version='0.1.0',
    description='''Cython implementations of Gibbs sampling for latent
    Dirichlet allocation and its supervised variants''',
    url='https://code.savvysherpa.com/SavvysherpaResearch/lda-cython',
    author='Berton Earnshaw',
    author_email='bearnshaw@savvysherpa.com',
    packages=[
        'lda_cython',
        'pypolyagamma',
    ],
    install_requires=[
        'cython >= 0.20.1',
        'cythongsl',
        'numpy',
        'scipy',
    ],
    ext_modules=cythonize(extensions),
    include_package_data=True,
)
