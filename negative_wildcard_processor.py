import re

class NegativeWildcardProcessor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "positive" : ("STRING", {"forceInput":True, "default": "", "multiline": True}),
                "negative" : ("STRING", {"forceInput":True, "default": "", "multiline": True})
            },
        }

    RETURN_TYPES = ('STRING','STRING',)
    RETURN_NAMES = ('text_positive','text_negative',)
    FUNCTION = "process_negative_wildcards"
    CATEGORY = "Dynamic Prompts"

    def process_negative_wildcards(self, positive, negative):
        # Pattern to match <! anything !>
        pattern = r"<!(.*?)!>"
        
        # Find all matches of the pattern in the positive string
        matches = re.findall(pattern, positive)
        
        # Remove all occurrences of the pattern from the positive string
        text_positive = re.sub(r"<!.*?!>", "", positive)
        text_positive = re.sub(r"<lora.*?>", "", text_positive)
        
        # Append all matches to the end of the negative string
        text_negative = negative
        for match in matches:
            text_negative += " " + match
        
        return (text_positive, text_negative,)

class CustomTokenPreprocessor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "token" : ("STRING", {"default": "", "multiline": False}),
                "source" : ("STRING", {"forceInput":True, "default": "", "multiline": True}),
                "target" : ("STRING", {"forceInput":True, "default": "", "multiline": True})
            },
        }

    RETURN_TYPES = ('STRING','STRING',)
    RETURN_NAMES = ('processed_source','processed_target',)
    FUNCTION = "process_custom_token"
    CATEGORY = "Dynamic Prompts"

    def process_custom_token(self, token, source, target):
        # Pattern to match <! anything !>
        pattern = r"<" + token + "(.*?)" + token + ">"
        
        # Find all matches of the pattern in the positive string
        matches = re.findall(pattern, source)
        
        # Remove all occurrences of the pattern from the positive string
        processed_source = re.sub(r"<" + token + ".*?" + token + ">", "", source)
        
        # Append all matches to the end of the negative string
        processed_target = target
        for match in matches:
            processed_target += " " + match
        
        return (processed_source, processed_target,)
