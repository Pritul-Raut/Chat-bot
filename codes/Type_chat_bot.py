import random
import openai

api_key="**********"
def ai(prompt):
    openai.api_key = api_key
    text=f"chat gpt response : \n###\n{prompt}\n###"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    ans = response["choices"][0]["text"]
    print(ans)
    text+=ans

# if not os.path.exists(("openai respnses")):
#    os.mkdir("open ai responses")

    with open(f"openai responses/prompt-{random.randint(1,200)}", 'w') as f:
        f.write(text)


while True:
    prompt=input("enter prompt :")
    ai(prompt)
    print("Answer completed \n")