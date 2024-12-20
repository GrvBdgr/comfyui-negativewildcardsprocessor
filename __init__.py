from .negative_wildcard_processor import NegativeWildcardProcessor, CustomTokenPreprocessor
NODE_CLASS_MAPPINGS = { "neg_wildcard_processor" : NegativeWildcardProcessor, "custom_token_processor" : CustomTokenPreprocessor }
NODE_DISPLAY_NAME_MAPPINGS = { "neg_wildcard_processor" : "Negative Wildcard Processor", "custom_token_processor" : "Custom Token Processor" }
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
