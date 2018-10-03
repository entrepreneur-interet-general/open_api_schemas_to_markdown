from setuptools import setup

setup(
    name='open_api_schemas_to_markdown',
    license='MIT',
    packages=['open_api_schemas_to_markdown'],
    version='0.3',
    description='Generate Markdown documentation from OpenAPI 3 Components Schemas',
    author='Antoine Augusti',
    author_email='hi@antoine-augusti.fr',
    url='https://github.com/entrepreneur-interet-general/open_api_schemas_to_markdown',
    scripts=['bin/oa-to-md'],
    keywords=['openapi', 'documentation', 'markdown', 'gfm'],
    install_requires=['PyYAML', 'future', 'yamlordereddictloader'],
    extras_require={'dev': ['nose']},
    python_requires='>=2.7, <4',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ]
)
