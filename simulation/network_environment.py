from network_packet import NetworkPacket
from generate_hex_id import generate_hex_id

class NetworkEnvironment:

    def __init__(
        self,
        nodes,
    ):
        
        self.nodes = nodes

        # 0.1s per step
        self.step_time="0.1"

        self.step_count = 0

    def step(self):  

        self.step_count += 1   

        if self.step_count == 3:

            self.nodes[-1]["node"].inbox.append(NetworkPacket(
                self.nodes[0]["node"].node_id,
                self.nodes[-1]["node"].node_id,
                generate_hex_id,
                {
                    "data": "random string data"
                },
                "DATA"
            ))

            print(self.nodes[-1]["node"].inbox)
        
        for node in self.nodes:

            if node["agent_type"] == "machine": 
                
                observation = {"outbox": node["node"].outbox, "inbox": node["node"].inbox}

                action = node["agent"].select_action(observation)

                print(f"Step: {self.step_count} {node['id']}: {action['type']}")

                if action["type"] == "SEND_ACK": 

                    ack_packet = NetworkPacket(action["destination_id"], action["sender_id"], action["packet_id"], action["payload"], action["type"])




        

