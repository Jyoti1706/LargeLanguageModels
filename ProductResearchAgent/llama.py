import modal
from modal import App, Volume, Image

# Initialize the Modal App
app = modal.App("llama")

# Define the image with necessary dependencies
image = Image.debian_slim().pip_install("torch", "transformers", "bitsandbytes", "accelerate")

# Define secrets to be used
secrets = [modal.Secret.from_name("hf-secret")]

# Specify the GPU type to be used
GPU = "T4"

# Specify the model name
MODEL_NAME = "meta-llama/Meta-Llama-3.1-8B" 

# Define the function with specified image, secrets, GPU, and timeout
@app.function(image=image, secrets=secrets, gpu=GPU, timeout=1800)
def generate(prompt: str) -> str:
    """
    Generate text based on the given prompt using a pre-trained model.

    Args:
        prompt (str): The input text prompt.

    Returns:
        str: The generated text.
    """
    import os
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, set_seed

    # Quantization configuration
    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_quant_type="nf4"
    )

    # Load the tokenizer and the model
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"
    
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME, 
        quantization_config=quant_config,
        device_map="auto"
    )

    # Set random seed for reproducibility
    set_seed(42)

    # Encode the prompt text to tensor format
    inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    
    # Create an attention mask
    attention_mask = torch.ones(inputs.shape, device="cuda")

    # Generate text from the model
    outputs = model.generate(inputs, attention_mask=attention_mask, max_new_tokens=5, num_return_sequences=1)
    
    # Decode the output text and return
    return tokenizer.decode(outputs[0])
