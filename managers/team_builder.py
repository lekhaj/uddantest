class TeamBuilder(object):
    def __init__(self, player_ctrl, user_ctrl):
        self.player_cntrl = player_ctrl
        self.user_ctrl = user_ctrl

    def add_player(self, user, player):
        if user.is_teamfinal:
            return "Error:: team is finalized"
        if user.credit > player.credit_worth:
            return "Error:: not enough credit"
        if self.user_ctrl.check_player_isin(user, player):
            return "Error:: player already in"
        if len(user.team) == 11:
            return "Error:: team full"

        self.user_ctrl.add_player(user, player)
        return "Success added player " + player.name

    def remove_player(self, user, player):
        self.user_ctrl.remove_player(user, player)

    def finalize_team(self, user):
        if user.curr_batsmans < 3:
            return "Error:: change team add more bastman"
        if user.curr_bowlers < 3:
            return "Error:: change team add more bowlers"
        if user.curr_keepers < 1:
            return "Error:: change team add more keepers"
        user.is_teamfinal = True