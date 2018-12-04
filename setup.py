from setuptools import setup

setup(
  name='markupsExtended',
  description="Add parsers to markups v3",
  version='0.0.1',
  author='a-mt',
  url="https://github.com/a-mt/markupsExtended",
  entry_points={
    'pymarkups': [
        'GithubMarkdown=markupsExtended:GithubMarkdownMarkup'
    ],
  }
)
