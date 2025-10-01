class Environment:

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
        
        for node in self.nodes:

            if node["agent_type"] == "machine": 

                observation = {"outbox": node["node"].outbox, "inbox": node["node"].inbox}

                action = node["agent"].select_action(observation)

                print(f"Step: {self.step_count} {node['id']}: {action}")




        

