from setuptools import setup

setup(
    name='open_api_schemas_to_markdown',
    license='MIT',
    packages=['open_api_schemas_to_markdown'],
    version='0.1',
    description='Generate Markdown documentation from OpenAPI 3 Components Schemas',
    author='Antoine Augusti',
    author_email='hi@antoine-augusti.fr',
    url='https://github.com/entrepreneur-interet-general/open_api_schemas_to_markdown',
    scripts=['bin/oa-to-md'],
    keywords=['openapi', 'documentation', 'markdown', 'gfm'],
    install_requires=['PyYAML', 'future', 'yamlordereddictloader'],
    extras_require={'dev': ['nose']}
)
