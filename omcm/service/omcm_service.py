class OmcResourceAction:
    def __init__(self, resource_action):
        self.action = resource_action

    def get_resource(self):
        return self.action.__self__

    def get_context(self):
        return self.get_resource().context

    def execute(self):
        return self.action()

    def get_commands(self):
        return self.get_context().get('all')

class ContentBuilder:
    def build_content(self):
        pass

    def build_list(self):
        pass