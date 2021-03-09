class User(object):
    def __init__(self, id, name, is_admin):
        self.user_id = id
        self.name = name
        self.is_admin = is_admin
        self.team = []
        self.curr_batsmans = 0
        self.curr_bowlers = 0
        self.curr_keepers = 0
        self.credit = 100
        self.is_teamfinal = False