from autogen import config_list_from_json, UserProxyAgent, AssistantAgent, Completion, Cache
import autogen

config_list = config_list_from_json(
    env_or_file="OAI_CONFIG_LIST"
)

llm_config = {"timeout": 600,
              "cache_seed": 42,
              "config_list": config_list,
              "temperature": 0, }

# User proxy Agent
user_proxy_agent = UserProxyAgent(
    name="user_proxy_agent",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "coding",
                           "use_docker": False}
)

# Assistant agent
assistant_agent = AssistantAgent(
    name="assistant_agent",
    llm_config=llm_config
)

# Use Redis as cache
with Cache.redis(redis_url="redis://localhost:6379/0") as cache:
    user_proxy_agent.initiate_chat(recipient=assistant_agent,
                                   message="use the dataset https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv, "
                                           "plot a graph for weather season (e.g rain, snow) Vs no of days and also "
                                           "provide insights as what "
                                           "months are generally sunny. ")


#message="Plot YTD performance between tesla and amazon")
#https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv
'''message = "use the dataset https://raw.githubusercontent.com/VikramSuriyanarayanan"
"/Machine-learning-approaches-for-crop-yield-prediction/master/dataset.csv, "
"plot a graph for yield/area Vs regions and also provide insights as what "
"features (e.g water, pesticides etc) are most important to increase "
"yield/area metrics.")'''

'''message="use the dataset https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv, "
                                       "plot a graph for weather season (e.g rain, snow) Vs no of days and also provide insights as what "
                                       "months are generally sunny. ")'''