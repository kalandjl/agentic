from typing import Literal

# Network node/machine controlled by ML agents
class Node:

    def __init__(
        self, 
        agent,
        node_id: int,
        node_type: Literal["rl", "machine"]
    ):
        
        # package inboxes and outboxes
        self.inbox = []
        self.outbox = []

        self.node_id = node_id
        
        self.agent = agent

        self.node_type = node_type

        self.staged_packets = []

    def recieve_packet(self, packet):

        self.inbox.append(packet)

    def get_observation_data(self):

        return {"outbox": self.outbox, "inbox": self.inbox}
    
    def stage_packet_for_sending(self, packet):

        self.staged_packets.append(packet)

    def reset(self):

        self.inbox = []
        self.outbox = self.staged_packets
            