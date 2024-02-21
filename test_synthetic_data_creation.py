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

message = "You are synthetic data generator. Create a csv dataset containing 50000 records with the following columns " \
          "and " \
          "type: customer_id - UUID, customer_name - String, datetimestamp - datetime, beem_height - float, " \
          "light_visibility - " \
          "boolean, speed - float, blur - boolean, is_fallback - boolean. The criteria to populate is_fallback column " \
          "as true are as follows:" \
          "speed > 10.0, blur - true, light_visibility - true, beem_height > 3.0. Even if one of the 3 criterias is " \
          "true, " \
          "then is_fallback column will be true" \
          " Generate mixed set of records with " \
          "is_fallback true and false. Save the dataset as customer_records_take2.csv"

# Use Redis as cache
with Cache.redis(redis_url="redis://localhost:6379/0") as cache:
    user_proxy_agent.initiate_chat(recipient=assistant_agent,
                                   message=message)

# message="Plot YTD performance between tesla and amazon")
# https://raw.githubusercontent.com/vega/vega/main/docs/data/seattle-weather.csv
'''message = "use the dataset https://raw.githubusercontent.com/VikramSuriyanarayanan"
"/Machine-learning-approaches-for-crop-yield-prediction/master/dataset.csv, "
"plot a graph for yield/area Vs regions and also provide insights as what "
"features (e.g water, pesticides etc) are most important to increase "
"yield/area metrics.")'''
