from model.agents import Agents

class AgentController:
    @staticmethod
    def add_agent(first_name, last_name, email, phone, wechat, agency_name):
        return Agents.add_agent(first_name, last_name, email, phone, wechat, agency_name)
    @staticmethod
    def get_all_agents():
        return Agents.get_all_agents()
    @staticmethod
    def get_agent_details(agent_id):
        return Agents.get_agent_details(agent_id)

    @staticmethod
    def update_agent(first_name, last_name, email, phone, wechat, agency_name):
        return Agents.update_agent(first_name, last_name, email, phone, wechat, agency_name)
    @staticmethod
    def get_agent_id_by_user_id(user_id):
        return Agents.get_agent_id_by_user_id(user_id)
    