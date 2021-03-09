from controllers.player_controller import *
from controllers.user_controller import *

from services.player_service import *
from services.user_service import *

from managers.team_builder import *

player_payload = [  {'id': 1, 'name': "sach", 'type': 1, 'credit_worth': 15},
                    {'id': 2, 'name': "gang", 'type': 1, 'credit_worth': 10},
                    {'id': 3, 'name': "dra", 'type': 1, 'credit_worth': 9},
                    {'id': 4, 'name': "lax", 'type': 1, 'credit_worth': 8},
                    {'id': 5, 'name': "lara", 'type': 1, 'credit_worth': 8},
                    {'id': 6, 'name': "mcgrath", 'type': 2, 'credit_worth': 7},
                    {'id': 7, 'name': "kumble", 'type': 2, 'credit_worth': 11},
                    {'id': 8, 'name': "warne", 'type': 2, 'credit_worth': 6},
                    {'id': 9, 'name': "murali", 'type': 2, 'credit_worth': 9},
                    {'id': 10, 'name': "lee", 'type': 2, 'credit_worth': 7},
                    {'id': 11, 'name': "don", 'type': 1, 'credit_worth': 9},
                    {'id': 12, 'name': "walsh", 'type': 2, 'credit_worth': 8},
                    {'id': 13, 'name': "dhoni", 'type': 3, 'credit_worth': 6},
                    {'id': 14, 'name': "sang", 'type': 3, 'credit_worth': 3},
                    {'id': 15, 'name': "gilly", 'type': 3, 'credit_worth': 5}
]
user_payload = [{'id': 1, 'name': "test_user", "is_admin": False},
                {'id': 2, 'name': "test_admin", "is_admin": True}
]
points_payload = [  {'id': 1, 'points': 150},
                    {'id': 2, 'points': 110},
                    {'id': 3, 'points': 78},
                    {'id': 4, 'points': 150},
                    {'id': 4, 'points': 90},
                    {'id': 5, 'points': 50},
                    {'id': 6, 'points': 150},
                    {'id': 7, 'points': 80},
                    {'id': 8, 'points': 150},
                    {'id': 9, 'points': 150},
                    {'id': 10, 'points': 70},
                    {'id': 11, 'points': 150},
                    {'id': 12, 'points': 150},
                    {'id': 13, 'points': 80},
                    {'id': 14, 'points': 150},
                    {'id': 15, 'points': 150}
                ]
u_contr = UserController(UserService())
p_contr = PlayerController(PlayerService())

p_contr.add_player_list(player_payload)
p = p_contr.get_player_by_id(1)
print(p.name)

user = u_contr.add_user(user_payload[0]["id"], user_payload[0]["name"], user_payload[0]["is_admin"])
admin = u_contr.add_user(user_payload[1]["id"], user_payload[1]["name"], user_payload[1]["is_admin"])

print("user:: " + user.name + " admin:: " + admin.name)

team_builder = TeamBuilder(p_contr, u_contr)
req_resp = team_builder.add_player(user, p)
print(req_resp)
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(2))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(15))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(7))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(8))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(9))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(14))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(3))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(10))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(11))
req_resp_temp = team_builder.add_player(user, p_contr.get_player_by_id(4))

req_resp = p_contr.update_player_points(admin, points_payload)
print(req_resp)

req_resp = u_contr.show_team_points(user)
print(req_resp)

