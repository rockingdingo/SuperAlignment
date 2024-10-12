# SuperAlignment package

This is the official github repo of pypi package SuperAlignment (https://pypi.org/project/SuperAlignment). 

Motivated by OpenAI's alignment paper "WEAK-TO-STRONG GENERALIZATION: ELICITING STRONG CAPABILITIES WITH WEAK SUPERVISION"(https://openai.com/index/weak-to-strong-generalization/), we feel that it's a very interesting direction to define some common interface to train/eval superalignment models in this new area. Right now it has just started from scratch and you are very welcome to contact us if you have any cool ideas that would like to participate and collabratively commit to this repo. 



```
pip install SuperAlignment
```

```
import SuperAlignment as sa

input_dict = {"text": "SuperAlignment"}

res = sa.api(input_dict, model=None, api_name="ArxivPaperAPI", start=0, max_results = 3)
paper_list = json.loads(res["text"])
print ("###### Text to Image Recent Paper List:")
for (i, paper_json) in enumerate(paper_list):
    print ("### PAPER %d" % (i+1))
    print (paper_json)


```

### Common Interface of SuperAlignment Application

```

class YourSuperAlignmentAPI(BaseAPI):
    """docstring for ClassName"""
    def __init__(self, configs):
        super(YourSuperAlignmentAPI, self).__init__(configs)
        self.name = "xxxxx"

    def api(self, input_dict, model, kwargs):
        """
            Args:
                input_dict: dict, multi-modal input text, image, audio and video
                model: huggingface model of tf or pytoch
                kwargs: key-value args
            Return:
                res_dict: dict, multi-modal text text, image, audio and video
        """
        res_dict={}
        try:
            input_text = input_dict["text"]   # str
            input_image = input_dict["image"] # image path
            input_audio = input_dict["audio"] # audio path
            input_video = input_dict["video"] # video path

            res_dict["text"] = None
            res_dict["image"] = None
            res_dict["audio"] = None
            res_dict["video"] = None
        except Exception as e:
            print (e)
        return res_dict


```

### SuperAlignment Losses


```
import torch
import torch.nn as nn
import torch.nn.functional as F

def auxConfidentLoss(alpha, t, x_weak, x_strong):
    """
        AUXILIARY CONFIDENCE LOSS as in weak to strong generalization paper
    """
    ce_loss = nn.CrossEntropyLoss()
    x_strong_ind = torch.relu(x_strong - t)
    aux_loss = alpha * ce_loss(x_strong, x_weak) + (1-alpha) * ce_loss(x_strong, x_strong_ind)
    return aux_loss


```




### Awesome SuperAlignment Papers and Projects

#### 2024 SuperAlignment Paper

|  PAPER  | URL  |
|  ----  | ----  |
| WEAK-TO-STRONG GENERALIZATION: ELICITING STRONG CAPABILITIES WITH WEAK SUPERVISION | https://cdn.openai.com/papers/weak-to-strong-generalization.pdf |
| Strong and weak alignment of large language models with human values | https://arxiv.org/pdf/2408.04655 |
| SUPER(FICIAL)-ALIGNMENT: STRONG MODELS MAY DECEIVE WEAK MODELS IN WEAK-TO-STRONG GENERALIZATION | https://arxiv.org/pdf/2406.11431 |
| SELF-PLAY WITH EXECUTION FEEDBACK: IMPROVING INSTRUCTION-FOLLOWING CAPABILITIES OF LARGE LANGUAGE MODELS | https://arxiv.org/pdf/2406.13542 |
| Quantifying the Gain in Weak-to-Strong Generalization | https://arxiv.org/abs/2405.15116 |
| A Superalignment Framework in Autonomous Driving with Large Language Models | https://arxiv.org/abs/2406.05651 |
| A Moral Imperative: The Need for Continual Superalignment of Large Language Models | https://arxiv.org/abs/2403.14683 |
| Vision Superalignment: Weak-to-Strong Generalization for Vision Foundation Models | https://arxiv.org/abs/2402.03749 |
| Improving Weak-to-Strong Generalization with Scalable Oversight and Ensemble Learning | https://arxiv.org/abs/2402.00667 |


### AI Services Reviews and Ratings <br>
##### Chatbot
[OpenAI o1 Reviews](http://www.deepnlp.org/store/pub/pub-openai-o1) <br>
[ChatGPT User Reviews](http://www.deepnlp.org/store/pub/pub-chatgpt-openai) <br>
[Gemini User Reviews](http://www.deepnlp.org/store/pub/pub-gemini-google) <br>
[Perplexity User Reviews](http://www.deepnlp.org/store/pub/pub-perplexity) <br>
[Claude User Reviews](http://www.deepnlp.org/store/pub/pub-claude-anthropic) <br>
[Qwen AI Reviews](http://www.deepnlp.org/store/pub/pub-qwen-alibaba) <br>
[Doubao Reviews](http://www.deepnlp.org/store/pub/pub-doubao-douyin) <br>
[ChatGPT Strawberry](http://www.deepnlp.org/store/pub/pub-chatgpt-strawberry) <br>
[Zhipu AI Reviews](http://www.deepnlp.org/store/pub/pub-zhipu-ai) <br>
##### AI Image Generation
[Midjourney User Reviews](http://www.deepnlp.org/store/pub/pub-midjourney) <br>
[Stable Diffusion User Reviews](http://www.deepnlp.org/store/pub/pub-stable-diffusion) <br>
[Runway User Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[GPT-5 Forecast](http://www.deepnlp.org/store/pub/pub-gpt-5) <br>
[Flux AI Reviews](http://www.deepnlp.org/store/pub/pub-flux-1-black-forest-lab) <br>
[Canva User Reviews](http://www.deepnlp.org/store/pub/pub-canva) <br>
##### AI Video Generation
[Luma AI](http://www.deepnlp.org/store/pub/pub-luma-ai) <br>
[Pika AI Reviews](http://www.deepnlp.org/store/pub/pub-pika) <br>
[Runway AI Reviews](http://www.deepnlp.org/store/pub/pub-runway) <br>
[Kling AI Reviews](http://www.deepnlp.org/store/pub/pub-kling-kwai) <br>
[Dreamina AI Reviews](http://www.deepnlp.org/store/pub/pub-dreamina-douyin) <br>
##### AI Education
[Coursera Reviews](http://www.deepnlp.org/store/pub/pub-coursera) <br>
[Udacity Reviews](http://www.deepnlp.org/store/pub/pub-udacity) <br>
[Grammarly Reviews](http://www.deepnlp.org/store/pub/pub-grammarly) <br>
##### Robotics
[Tesla Cybercab Robotaxi](http://www.deepnlp.org/store/pub/pub-tesla-cybercab) <br>
[Tesla Optimus](http://www.deepnlp.org/store/pub/pub-tesla-optimus) <br>
[Figure AI](http://www.deepnlp.org/store/pub/pub-figure-ai) <br>
[Unitree Robotics Reviews](http://www.deepnlp.org/store/pub/pub-unitree-robotics) <br>
[Waymo User Reviews](http://www.deepnlp.org/store/pub/pub-waymo-google) <br>
[ANYbotics Reviews](http://www.deepnlp.org/store/pub/pub-anybotics) <br>
[Boston Dynamics](http://www.deepnlp.org/store/pub/pub-boston-dynamic) <br>
##### AI Tools
[DeepNLP AI Tools](http://www.deepnlp.org/store/pub/pub-deepnlp-ai) <br>
##### AI Widgets
[Apple Glasses](http://www.deepnlp.org/store/pub/pub-apple-glasses) <br>
[Meta Glasses](http://www.deepnlp.org/store/pub/pub-meta-glasses) <br>
[Apple AR VR Headset](http://www.deepnlp.org/store/pub/pub-apple-ar-vr-headset) <br>
[Google Glass](http://www.deepnlp.org/store/pub/pub-google-glass) <br>
[Meta VR Headset](http://www.deepnlp.org/store/pub/pub-meta-vr-headset) <br>
[Google AR VR Headsets](http://www.deepnlp.org/store/pub/pub-google-ar-vr-headset) <br>
##### Social
[Character AI](http://www.deepnlp.org/store/pub/pub-character-ai) <br>
##### Self-Driving
[BYD Seal](http://www.deepnlp.org/store/pub/pub-byd-seal) <br>
[Tesla Model 3](http://www.deepnlp.org/store/pub/pub-tesla-model-3) <br>
[BMW i4](http://www.deepnlp.org/store/pub/pub-bmw-i4) <br>
[Baidu Apollo Reviews](http://www.deepnlp.org/store/pub/pub-baidu-apollo) <br>
[Hyundai IONIQ 6](http://www.deepnlp.org/store/pub/pub-hyundai-ioniq-6) <br>


### Related Blogs <br>
[Open AI Weak to Strong Generalization](https://openai.com/index/weak-to-strong-generalization/) <br>
[Introduction to multimodal generative models](http://www.deepnlp.org/blog/introduction-to-multimodal-generative-models) <br>
[Generative AI Search Engine Optimization](http://www.deepnlp.org/blog/generative-ai-search-engine-optimization-how-to-improve-your-content) <br>
[AI Image Generator User Reviews](http://www.deepnlp.org/store/image-generator) <br>
[AI Video Generator User Reviews](http://www.deepnlp.org/store/video-generator) <br>
[AI Chatbot & Assistant Reviews](http://www.deepnlp.org/store/chatbot-assistant) <br>
[Best AI Tools User Reviews](http://www.deepnlp.org/store/pub/) <br>
