import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "0DB57CE3-99D1-4FB4-A7F4-DBA0668B3E70",
  "name": "Zork made by me",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631368765864,
  "passages": [
    {
      "name": "Starting Room",
      "tags": "",
      "id": "1",
      "text": "You wake up to find yourself In a dark and mysterious cave. You have no idea how you got there, but you do know one thing for certain. You need to get out of here. There are four paths that you are able to go through.\n[[NORTH->North Entry Way]]\n[[SOUTH->South Entry Way]]\n[[EAST->East Entry Way]]\n[[WEST->West Entry Way]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "North Entry Way",
          "original": "[[NORTH->North Entry Way]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "South Entry Way",
          "original": "[[SOUTH->South Entry Way]]"
        },
        {
          "linkText": "EAST",
          "passageName": "East Entry Way",
          "original": "[[EAST->East Entry Way]]"
        },
        {
          "linkText": "WEST",
          "passageName": "West Entry Way",
          "original": "[[WEST->West Entry Way]]"
        }
      ],
      "hooks": [],
      "cleanText": "You wake up to find yourself In a dark and mysterious cave. You have no idea how you got there, but you do know one thing for certain. You need to get out of here. There are four paths that you are able to go through."
    },
    {
      "name": "North Entry Way",
      "tags": "",
      "id": "2",
      "text": "The North Entry Way leads to a long tunnel. It is very dark, so you can't see much of anything. \n[[NORTH->End of North Tunnel]]\n[[SOUTH->Starting Room]]",
      "links": [
        {
          "linkText": "NORTH",
          "passageName": "End of North Tunnel",
          "original": "[[NORTH->End of North Tunnel]]"
        },
        {
          "linkText": "SOUTH",
          "passageName": "Starting Room",
          "original": "[[SOUTH->Starting Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The North Entry Way leads to a long tunnel. It is very dark, so you can't see much of anything."
    },
    {
      "name": "South Entry Way",
      "tags": "",
      "id": "3",
      "text": "The South Entry Way reeks of an awful stench you can't describe. The ground is also wet. The only way is forward or back.\n[[SOUTH->South Tunnel]]\n[[NORTH->Starting Room]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "South Tunnel",
          "original": "[[SOUTH->South Tunnel]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "Starting Room",
          "original": "[[NORTH->Starting Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The South Entry Way reeks of an awful stench you can't describe. The ground is also wet. The only way is forward or back."
    },
    {
      "name": "East Entry Way",
      "tags": "",
      "id": "4",
      "text": "The East Entry way leads you to a dark tunnel. It smells like mildew, but something else as well. You see a light at the end of the tunnel.\n[[EAST->Blob Worship Room]]\n[[WEST->Starting Room]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "Blob Worship Room",
          "original": "[[EAST->Blob Worship Room]]"
        },
        {
          "linkText": "WEST",
          "passageName": "Starting Room",
          "original": "[[WEST->Starting Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The East Entry way leads you to a dark tunnel. It smells like mildew, but something else as well. You see a light at the end of the tunnel."
    },
    {
      "name": "West Entry Way",
      "tags": "",
      "id": "5",
      "text": "The West Entry Way leads you to a  dark tunnel. It smells like mildew. The only way is forward.\n[[WEST->West Tunnel]]\n[[EAST->Starting Room]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "West Tunnel",
          "original": "[[WEST->West Tunnel]]"
        },
        {
          "linkText": "EAST",
          "passageName": "Starting Room",
          "original": "[[EAST->Starting Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "The West Entry Way leads you to a  dark tunnel. It smells like mildew. The only way is forward."
    },
    {
      "name": "South Tunnel",
      "tags": "",
      "id": "6",
      "text": "The smell starts to get stronger the further you go. It gets to a point where you have to hold your breath. There are puddles of liquid on the ground. You start to see a light at the end of the tunnel\n[[SOUTH->Blob Room]]\n[[NORTH->South Entry Way]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "Blob Room",
          "original": "[[SOUTH->Blob Room]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "South Entry Way",
          "original": "[[NORTH->South Entry Way]]"
        }
      ],
      "hooks": [],
      "cleanText": "The smell starts to get stronger the further you go. It gets to a point where you have to hold your breath. There are puddles of liquid on the ground. You start to see a light at the end of the tunnel"
    },
    {
      "name": "Blob Room",
      "tags": "",
      "id": "7",
      "text": "At the end of the tunnel, you find the source of the horrible smell. A giant blob sits idle. There are a few people who stand around the blob, all admiring it. You see another tunnel with a bright light coming from it.\n[[SOUTH->Exit]]\n[[NORTH->South Tunnel]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "Exit",
          "original": "[[SOUTH->Exit]]"
        },
        {
          "linkText": "NORTH",
          "passageName": "South Tunnel",
          "original": "[[NORTH->South Tunnel]]"
        }
      ],
      "hooks": [],
      "cleanText": "At the end of the tunnel, you find the source of the horrible smell. A giant blob sits idle. There are a few people who stand around the blob, all admiring it. You see another tunnel with a bright light coming from it."
    },
    {
      "name": "Blob Worship Room",
      "tags": "",
      "id": "8",
      "text": "At the end of the tunnel, you are met by a strange room. There is a statue of what seems to be some sort of blob. There are a few people worshiping the statue, but they pay no mind to you. The statue has a strange, green substance on it.\n[[WEST->East Entry Way]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "East Entry Way",
          "original": "[[WEST->East Entry Way]]"
        }
      ],
      "hooks": [],
      "cleanText": "At the end of the tunnel, you are met by a strange room. There is a statue of what seems to be some sort of blob. There are a few people worshiping the statue, but they pay no mind to you. The statue has a strange, green substance on it."
    },
    {
      "name": "Exit",
      "tags": "",
      "id": "9",
      "score": 100,
      "text": "At the end of the tunnel, you make your way back to the outside world. You made it out of the cave!!!",
      "links": [],
      "hooks": [],
      "cleanText": "At the end of the tunnel, you make your way back to the outside world. You made it out of the cave!!!"
    },
    {
      "name": "End of North Tunnel",
      "tags": "",
      "id": "10",
      "text": "You make it to the end of the tunnel, only to be met with a dead end. The path has been blocked off by large debris.\n[[SOUTH->North Entry Way]]",
      "links": [
        {
          "linkText": "SOUTH",
          "passageName": "North Entry Way",
          "original": "[[SOUTH->North Entry Way]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make it to the end of the tunnel, only to be met with a dead end. The path has been blocked off by large debris."
    },
    {
      "name": "West Tunnel",
      "tags": "",
      "id": "11",
      "text": "The West tunnel is long, but you see a light at the end of it. You also start to hear strange music.\n[[WEST->End of West Tunnel]]\n[[EAST->West Entry Way]]",
      "links": [
        {
          "linkText": "WEST",
          "passageName": "End of West Tunnel",
          "original": "[[WEST->End of West Tunnel]]"
        },
        {
          "linkText": "EAST",
          "passageName": "West Entry Way",
          "original": "[[EAST->West Entry Way]]"
        }
      ],
      "hooks": [],
      "cleanText": "The West tunnel is long, but you see a light at the end of it. You also start to hear strange music."
    },
    {
      "name": "End of West Tunnel",
      "tags": "",
      "id": "12",
      "score": 20,
      "text": "At the end of the West tunnel, you find yourself in a large room. There is a tiny goblin dancing. The goblin sees you and performs a little dance for you\n[[EAST->West Tunnel]]",
      "links": [
        {
          "linkText": "EAST",
          "passageName": "West Tunnel",
          "original": "[[EAST->West Tunnel]]"
        }
      ],
      "hooks": [],
      "cleanText": "At the end of the West tunnel, you find yourself in a large room. There is a tiny goblin dancing. The goblin sees you and performs a little dance for you"
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}


# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("Moves: " + str(moves) + ", Score: " + str(score))
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Starting Room"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
	moves += 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	if "score" in current_location:
		score = score + current_location["score"]
	render(current_location, score, moves)
	if current_location["name"] == "Exit":
		break
	response = get_input()


print("Thanks for playing!")