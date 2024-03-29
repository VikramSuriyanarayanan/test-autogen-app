from typing import Literal
from typing_extensions import Annotated

import autogen

config_list = autogen.config_list_from_json(
    env_or_file="OAI_CONFIG_LIST"
)

llm_config = {"timeout": 600,
              "cache_seed": 42,
              "config_list": config_list,
              "temperature": 0, }

llm_config = {
    "config_list": config_list,
    "timeout": 120,
}

chatbot = autogen.AssistantAgent(
    name="chatbot",
    system_message="For currency exchange tasks, only use the functions you have been provided with. Reply TERMINATE "
                   "when the task is done.",
    llm_config=llm_config,
)

# create a UserProxyAgent instance named "user_proxy"
user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    is_termination_msg=lambda x: x.get("content", "") and x.get("content", "").rstrip().endswith("TERMINATE"),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    code_execution_config={"work_dir": "coding",
                           "use_docker": False}
)

CurrencySymbol = Literal["USD", "INR"]


def exchange_rate(base_currency: CurrencySymbol, quote_currency: CurrencySymbol) -> float:
    if base_currency == quote_currency:
        return 1.0
    elif base_currency == "USD" and quote_currency == "INR":
        return 1 / 83.0
    elif base_currency == "INR" and quote_currency == "USD":
        return 83.0
    else:
        raise ValueError(f"Unknown currencies {base_currency}, {quote_currency}")


@user_proxy.register_for_execution()
@chatbot.register_for_llm(description="Currency exchange calculator.")
def currency_calculator(
        base_amount: Annotated[float, "Amount of currency in base_currency"],
        base_currency: Annotated[CurrencySymbol, "Base currency"] = "USD",
        quote_currency: Annotated[CurrencySymbol, "Quote currency"] = "INR",
) -> str:
    quote_amount = exchange_rate(base_currency, quote_currency) * base_amount
    return f"{quote_amount} {quote_currency}"


user_proxy.initiate_chat(
    chatbot,
    message=
    "How much is 123.45 USD in INR?",
)