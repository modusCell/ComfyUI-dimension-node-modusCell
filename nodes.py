class DimensionProviderRatio:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dimension": (["512 x 512", "512 x 768", "768 x 512", "1024 x 1024", "1152 x 896", "896 x 1152", "1216 x 832", "832 x 1216", "1344 x 768", "768 x 1344", "1536 x 640", "640 x 1536", "1280 x 720"],),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("ratio_width", "ratio_height")
    FUNCTION = "prodvide_dimensions"
    OUTPUT_NODE = True
    CATEGORY = "DimensionProviderRatio"

    def prodvide_dimensions(self, dimension):
        dims = ["512x512", "512x768", "768x512", "1024x1024", "1152x896", "896x1152", "1216x832", "832x1216", "1344x768", "768x1344", "1536x640", "640x1536", "1280x720"]
        index = dims.index(dimension.replace(" ", ""))
        img_dims = dimension.split("x")
        return (int(img_dims[0]), int(img_dims[1]))

class DimensionProviderFree:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "width": ("INT", {"default": 512, "min": 1, "max": 10000}),
                "height": ("INT", {"default": 768, "min": 1, "max": 10000})
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("free_width", "free_height")
    FUNCTION = "prodvide_dimensions"
    OUTPUT_NODE = True
    CATEGORY = "DimensionProviderFree"

    def prodvide_dimensions(self, width, height):
        return (width, height)

class StringConcat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string_1": ("STRING", {"default": "", "multiline": False}),
                "string_2": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("STRING",)
    FUNCTION = "concat_string"
    OUTPUT_NODE = True
    CATEGORY = "concat_string"

    def concat_string(self, string_1, string_2):
        return (f'{string_1}, {string_2}',)


NODE_CLASS_MAPPINGS = {
    "DimensionProviderRatio modusCell": DimensionProviderRatio,
    "DimensionProviderFree modusCell": DimensionProviderFree,
    "String Concat modusCell": StringConcat,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Ratio": "Width and Height Node",
    "Free": "Width and Height Node"
}