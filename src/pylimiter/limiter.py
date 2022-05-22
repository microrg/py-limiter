class Client:
    def __init__(self, project_id, opts):
        self.project_id = project_id
        self.opts = opts

    def bind(self, plan_id, user_id):
        pass

    def feature(self, feature_id, user_id):
        pass

    def increment(self, feature_id, user_id):
        pass

    def decrement(self, feature_id, user_id):
        pass

    def set(self, feature_id, user_id, value):
        pass

    def feature_matrix(self):
        pass

    def usage(self, user_id):
        pass
