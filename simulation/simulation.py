from agents import DumbAgent
from node import Node

nodes = [
    # {
    #     "type": "rl",
    #     "agent": "",
    #     "id": "abcdef1234",
    #     "node": None
    # },
    {
        "type": "machine",
        "agent": DumbAgent("dumb_machine1"),
        "id": "dumb_machine1",
        "node": None
    },
        {
        "type": "machine",
        "agent": DumbAgent("dumb_machine2"),
        "id": "dumb_machine2",
        "node": None
    },
]

for node in nodes: 


    if node["type"] == "machine": node["agent"] == DumbAgent(node["id"])

    node["type"] = Node(node["agent"], node["id"], node["type"])