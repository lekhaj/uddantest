class PlayerController(object):
    def __init__(self, player_service):
        self.player_service = player_service

    def add_player(self, id, name, type):
        service = self.player_service
        return service.add_player(id,name,type)

    def add_player_list(self, player_list):
        for player_dict in player_list:
            self.add_player(player_dict["id"], player_dict["name"], player_dict["type"])

    def get_player_by_id(self, p_id):
        player = self.player_service.player_details.get(p_id)
        return player

    def update_player_points(self, user, points_dict):
        if user.is_admin:
            for points_data in points_dict:
                player = self.player_service.player_details.get(points_data["id"])
                player.points = points_data["points"]
            return "Success"
        else:
            return "Authorization Error ::"