class DimensionProvider:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "dimension": (["512 x 512", "512 x 768", "768 x 512", "1024 x 1024", "1152 x 896", "896 x 1152", "1216 x 832", "832 x 1216", "1344 x 768", "768 x 1344", "1536 x 640", "640 x 1536"],),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "prodvide_dimensions"
    OUTPUT_NODE = True
    CATEGORY = "DimensionProvider"

    def prodvide_dimensions(self, dimension):
        dims = ["512x512", "512x768", "768x512", "1024x1024", "1152x896", "896x1152", "1216x832", "832x1216", "1344x768", "768x1344", "1536x640", "640x1536"]
        index = dims.index(dimension.replace(" ", ""))
        img_dims = dimension.split("x")
        return (int(img_dims[0]), int(img_dims[1]))


NODE_CLASS_MAPPINGS = {
    "DimensionProvider modusCell": DimensionProvider,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "DimensionProvider": "Width and Height Node"
}
