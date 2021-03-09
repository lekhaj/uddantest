class UserController(object):
    def __init__(self, user_service):
        self.user_service = user_service

    def add_user(self, id, name, is_admin):
        service = self.user_service
        return service.add_user(id,name,is_admin)

    def add_player(self, user, player):
        user.team.append(player)
        if player.type == 1:
            user.curr_batsmans += 1
        if player.type == 2:
            user.curr_bowlers += 1
        if player.type == 3:
            user.curr_keepers += 1
        user.credit -= player.credit_worth # use lock for this if necessary

    def check_player_isin(self, user, player):
        if player in user.team:
            return True
        else:
            return False

    def remove_player(self, user, player):
        if check_player_isin(user, player):
            user.team.remove(player)
            if player.type == 1:
                user.curr_batsmans -= 1
            if player.type == 2:
                user.curr_bowlers -= 1
            if player.type == 3:
                user.curr_keepers -= 1
            user.credit += player.credit_worth

    def show_team_points(self, user):
        team_points = 0
        for player in user.team:
            team_points += player.points
        return "your total team points after match is " + str(team_points)