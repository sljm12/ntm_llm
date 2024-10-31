from openai import OpenAI

system_prompt = """
You are a helpful, smart, kind, and efficient AI assistant. You always fulfill the user's requests to the best of your ability.
"""

prompt_template = """

The following is a Notice to Mariners extract.

Please extract the following information from it in JSON format. 

    "ntm_number"
    "notice_date"
    "event",
    "locations"
    "date_from"
    "date_to"
    "vessels"
    "other information"

Do not leave anything out. Please include all the vessels/details no matter how long.
Include all location coordinates. 
For date information please use the following format: YYYY-MM-DD.
For locations please use the GeoJSON format. 
Please convert the locations coordinates properly.
For vessels please include the following information:
    vessel_name
    call_sign
    flag
    type
    

Text:
{text}

"""

def create_openai_llm(prompt_template):
    def F(text):
        # Point to the local server
        client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

        prompt = prompt_template.format(text=text)
        
        completion = client.chat.completions.create(
            model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.01,
        )

        return extract_json(completion.choices[0].message.content)

    return F

def call_llm(text):
    # Point to the local server
    client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    prompt = prompt_template.format(text=text)
    
    completion = client.chat.completions.create(
        model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt}
    ],
    temperature=0.01,
    )

    return extract_json(completion.choices[0].message.content)

def extract_json(text):
    lines = text.split("\n")
    start = False
    
    results=''
    
    for l in lines:
        if l.startswith("```"):
            if start is False:
                start = True
                continue
            else:
                start = False
                return results
        if start:
            results = results + l
    
    return results