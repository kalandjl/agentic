from generate_hex_id import generate_hex_id

class DumbAgent:

    def __init__(self, machine_id):

        self.machine_id = machine_id

    def select_action(self, observation):

        for packet in observation["inbox"]:

            if packet.packet_type == "DATA":
                return {
                    "type": "SEND_ACK",
                    "sender_id": self.machine_id,
                    "destination_id": packet.sender_id,
                    "packet_id": generate_hex_id(),
                    "payload": {},
                }
            
        return {"type": "WAIT"}