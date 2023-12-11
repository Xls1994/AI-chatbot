# ！/usr/bin env python3
# -*- coding: utf-8 -*-
# author: yangyunlong time:2023/12/1

PROMPT_TEMPLATE = """
已知信息：
{context} 

根据上述已知信息，简洁和专业的来回答用户的问题。如果无法从中得到答案，请说 “根据已知信息无法回答该问题” 或 “没有提供足够的相关信息”，不允许在答案中添加编造成分，答案请使用中文。 
问题是：{question}"""

def generate_prompt(query, docs):
    context = []
    for index, doc in enumerate(docs):
        doc = doc.strip()
        f_prompt = "<{a}>: {b}".format(a=index + 1, b=doc)
        context.append(f_prompt)
    context = "\n".join(context)
    prompt = PROMPT_TEMPLATE.replace("{question}", query).replace("{context}", context)
    return prompt