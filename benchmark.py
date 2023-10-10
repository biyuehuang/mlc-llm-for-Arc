from mlc_chat import ChatModule
cm = ChatModule(model="./dist_13b/llama-2-13b-chat-hf-q4f16_1/params/", lib_path="./dist_13b/llama-2-13b-chat-hf-q4f16_1/llama-2-13b-chat-hf-q4f16_1-vulkan.so")
#cm = ChatModule(model="./dist/Llama-2-7b-chat-hf-q4f16_1/params/", lib_path="./dist/Llama-2-7b-chat-hf-q4f16_1/Llama-2-7b-chat-hf-q4f16_1-vulkan.so") #
output = cm.benchmark_generate("Once upon a time, there existed a little girl who liked to have adventures. She wanted to go to places and meet new people and have fun.", generate_length=128)
print(f"Generated text:\n{output}\n")
print(f"Statistics: {cm.stats()}")
