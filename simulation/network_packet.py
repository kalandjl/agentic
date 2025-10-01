
class NetworkPacket:

    def __init__(self, destination_id, sender_id, packet_id, payload, packet_type):
        
        self.destination_id = destination_id

        self.sender_id = sender_id

        self.payload = payload

        self.packet_id = packet_id

        self.packet_type = packet_type