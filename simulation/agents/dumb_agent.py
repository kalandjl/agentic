class DumbAgent:

    def __init__(self, machine_id):

        self.machine_id = machine_id

    def select_action(self, observation):

        for packet in observation["inbox"]:

            if packet.type == "DATA":
                return "SEND_ACK"
            
        return "WAIT"