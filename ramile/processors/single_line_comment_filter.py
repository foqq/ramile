from ramile.processors import LineFilterBase


class SingleLineCommentFilter(LineFilterBase):
    """ Filters out single line comments which start with '//'
    """

    def __init__(self, prefix: str):
        self.prefix = prefix

    def filter(self, file, line):
        if line.startswith(self.prefix):
            file.found_comment_line()
            return line, True
        return line, False
