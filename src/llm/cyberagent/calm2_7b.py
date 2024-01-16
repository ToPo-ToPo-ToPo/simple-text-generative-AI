
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import BitsAndBytesConfig
import platform
#====================================================================
# lineのベースを管理するクラス
#====================================================================
class Calm2_7b_Chat:

    #----------------------------------------------------------
    # コンストラクタ
    #----------------------------------------------------------
    def __init__(self, processor, load_bit_size, load_in_8bit=False, load_in_4bit=False, llm_int8_enable_fp32_cpu_offload=False):

        # モデル名の設定
        MODEL_NAME = "cyberagent/calm2-7b-chat"

        #
        self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

        # 量子化に関する設定
        quantization_config = BitsAndBytesConfig(llm_int8_enable_fp32_cpu_offload=llm_int8_enable_fp32_cpu_offload)

        # モデルの設定
        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME, 
            device_map=processor, 
            torch_dtype=load_bit_size, 
            load_in_8bit=load_in_8bit,
            load_in_4bit=load_in_4bit, 
            quantization_config=quantization_config,
            offload_folder="../offload_folder"
        )
    
    #----------------------------------------------------------
    # プロンプトの設定
    #----------------------------------------------------------
    def generate_prompt(self, question=None):

        prompt = f"USER: {question}\nASSISTANT: "

        return prompt
    
    #----------------------------------------------------------
    # 入力したpromptに対して回答を作成
    #----------------------------------------------------------
    def response(self, prompt=None):

        token_ids = self.tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")

        with torch.no_grad():
            output_ids = self.model.generate(
                token_ids.to(self.model.device),
                do_sample=True,
                max_new_tokens=256,
                temperature=0.7,
                repetition_penalty=1.1,
                pad_token_id=self.tokenizer.pad_token_id,
                bos_token_id=self.tokenizer.bos_token_id,
                eos_token_id=self.tokenizer.eos_token_id
            )

        output = self.tokenizer.decode(output_ids.tolist()[0][token_ids.size(1):])

        return output