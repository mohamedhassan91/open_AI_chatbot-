import openai 
openai.api_key = "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"
def chat_with_gbt(prompt):
    response = openai.ChatCompletion.create(
      model = "gpt-3.5-turbo",
      messages = [{"role":"user","content":prompt}]

    )
    return response.choices[0].maessage.content.strip()


if __name__ == "__main__":  
    while True:
      user_input = input("you:") 
      if user_input.lower() in ["quit","exit","bye"]:
         break 
      
      response = chat_with_gbt(user_input)

      print("chatbot:",response)

