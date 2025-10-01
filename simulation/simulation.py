from agents.dumb_agent import DumbAgent
from node.node import Node
from environment.environment import Environment

nodes = [
    # {
    #     "type": "rl",
    #     "agent": "",
    #     "id": "abcdef1234",
    #     "node": None
    # },
    {
        "agent_type": "machine",
        "agent": DumbAgent("dumb_machine1"),
        "id": "dumb_machine1",
        "node": None
    },
        {
        "agent_type": "machine",
        "agent": DumbAgent("dumb_machine2"),
        "id": "dumb_machine2",
        "node": None
    },
]


for node in nodes: 


    if node["agent_type"] == "machine": node["agent"] == DumbAgent(node["id"])

    node["node"] = Node(node["agent"], node["id"], node["agent_type"])

# Initialize simulation environment
environment = Environment(nodes)

for i in range(10):

    environment.step()