from setuptools import setup, find_packages

# Specify the project's metadata
setup(
    name='rsa-encryption',
    version='1.0',
    description='A simple implementation of RSA encryption in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/samyalder/rsa-encryption',
    author='Samy Alderson',
    author_email='samyalder@example.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='rsa encryption cryptography',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['cryptography'],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': ['rsa-encryption=main:main'],
    },
)