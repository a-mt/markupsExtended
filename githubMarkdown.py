#!/usr/bin/env python3

import re
import mistletoe
import markups.common as common
from markups.abstract import AbstractMarkup, ConvertedMarkup

from pygments import highlight
from pygments.styles import get_style_by_name as get_style
from pygments.lexers import get_lexer_by_name as get_lexer, guess_lexer
from pygments.formatters.html import HtmlFormatter

class GithubMarkdownMarkup(AbstractMarkup):

    name                 = 'Markdown'
    file_extensions      = ('.md', '.mkd', '.mkdn', '.mdwn', '.mdown', '.markdown')
    default_extension    = '.md'
    requested_extensions = []

    def __init__(self, filename):
        self.filename  = filename

    # Convert a Markdown text to HTML using mitletoe (GFM parser)
    def convert(self, text):

        def reanchor(match):
            return "[" + match.group(1) + "](" + match.group(2).replace(" ", "%20") + ")"

        text  = re.sub(r'\[([^]]*)\]\(([^)]+)\)', reanchor, text)
        body  = mistletoe.markdown(text, renderer=PygmentsRenderer) + '\n'

        return ConvertedMarkup(body)

# Highlight pre blocks using Pygments
class PygmentsRenderer(mistletoe.HTMLRenderer):
    formatter = HtmlFormatter()
    formatter.noclasses = True

    def __init__(self, *extras, style='default'):
        super().__init__(*extras)
        self.formatter.style = get_style(style)

    def render_block_code(self, token):
        code = token.children[0].content
        try:
            lexer = get_lexer(token.language) if token.language else guess_lexer(code)
            return highlight(code, lexer, self.formatter)
        except:
            return '<pre>' + code + '</pre>'
