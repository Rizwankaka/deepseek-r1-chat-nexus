import chainlit as cl
import ollama
import json

@cl.on_message
async def main(message: cl.Message):
    # Create a message dictionary instead of using Message objects directly
    messages = [{'role': 'user', 'content': str(message.content)}]
    
    # Create a message first
    msg = cl.Message(content="")
    await msg.send()

    # Create a stream with ollama
    stream = ollama.chat(
        model='deepseek-r1:1.5b',  # Use a model you have installed
        messages=messages,
        stream=True,
    )

    # Stream the response token by token
    for chunk in stream:
        if token := chunk['message']['content']:
            await msg.stream_token(token)
    
    # Update the message one final time
    await msg.update()

@cl.on_chat_start
async def start():
    await cl.Message(content="Hello! How can I help you today?").send()