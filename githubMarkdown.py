#!/usr/bin/env python3

import mistletoe
import markups.common as common
from markups.abstract import AbstractMarkup, ConvertedMarkup

class GithubMarkdownMarkup(AbstractMarkup):

    name                 = 'GithubMarkdown'
    file_extensions      = ('.md', '.mkd', '.mkdn', '.mdwn', '.mdown', '.markdown')
    default_extension    = '.mkd'
    requested_extensions = []

    def __init__(self, filename):
        self.filename  = filename

    def convert(self, text):
        title = ''
        body  = mistletoe.markdown(text) + '\n'

        # Determine stylesheet
        if any(extension.endswith('codehilite') for extension in self.requested_extensions):
            stylesheet = common.get_pygments_stylesheet('.codehilite')
        else:
            stylesheet = ''

        return ConvertedMarkup(body, title, stylesheet)
