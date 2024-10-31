from openai_llm import create_openai_llm

prompt_template = """
The following is a Notice to Mariners extract.

Please extract the following information from it in JSON format. Do not leave anything out. Please include all the vessels/details no matter how long.

    "ntm_number"
    "notice_date"
    "event",
    "locations"
    "date_from"
    "date_to"
    "vessels"
    "other information"


For date information please use the following format: YYYY-MM-DD.
For locations please use the GeoJSON format. 
For vessels please include the following information:
    vessel_name
    call_sign
    flag
    type
    

Text:
{text}
"""

call_llm = create_openai_llm(prompt_template)