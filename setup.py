from distutils.core import setup

setup(
    name='toggleproperties',
    version='0.1',
    description='Generic Django to toggle properties on objects',
    author='Salvatore Iovene',
    author_email='salvatore@iovene.com',
    license='Apache 2.0',
    packages=['toggleproperties', 'toggleproperties.templatetags'],
    package_data={
      'toggleproperties': ['templates/toggleproperties/*.html'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
