class CommentBlock(object):
    def __init__(self):
        self.params = {}
        self.retval_block = None
        self.description = None
        self.tags = {}

    def add_param_block (self, param_name, block):
        self.params[param_name] = block

    def set_return_block (self, block):
        self.tags['returns'] = block

    def set_description (self, description):
        self.description = description.strip();