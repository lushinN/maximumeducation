#pip install vk-api

import vk_api

token = 'vk1.a.lPoubjhbvPD80vPOVJrG2_BLFri6kPADtOD7BWRn0coXhHEN_iX1HjMVMBJ-C9w62YZabw1O6elP9TfP0VuYO8D_qBjFdyEQe9Ar1bRIlLRTOYxfDbSq9nXnWKfLlP5_ZpmIHEt1lxq90z9f5hXNSauIybSDTzV-42N_rBda3e-IgbLgn9OBJtGaVxv7S6vWDRdfr2AJyOF2751D_7GuQw'

vk = vk_api.VkApi(token=token)

messages = vk.method('messages.getConversations', {'count': 20, 'filter': 'unanswered'})

print(messages)