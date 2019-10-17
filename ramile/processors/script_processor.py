from ramile.processors import FileProcessorBase
from ramile.processors import BlankLineFilter
from ramile.processors.c_style_comment_block_filter import CStyleCommentBlockFilter
from ramile.processors.double_slash_comment_filter import DoubleSlashCommentFilter
from ramile.processors.single_line_comment_filter import SingleLineCommentFilter


class ScriptProcessor(FileProcessorBase):
    expected_extensions = ['.py', '.sh']
    header_template = '# __file__\n'

    def __init__(self):
        FileProcessorBase.__init__(self)
        self.filters.append(BlankLineFilter())
        self.filters.append(SingleLineCommentFilter('#'))
        return
