import re

class NegativeWildcardProcessor:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "positive" : ("STRING", {"default": "", "multiline": True}),
                "negative" : ("STRING", {"default": "", "multiline": True})
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