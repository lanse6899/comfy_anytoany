class anytoany:
    """
    通用映射节点：可以将任何输入映射到任何其他输入
    例如：小猫=3, 1=B, 小猫=B 等
    兼容所有ComfyUI版本
    使用字符串类型确保最大兼容性
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_a": ("STRING", {"multiline": False, "default": ""}),
                "input_b": ("STRING", {"multiline": False, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output_a", "output_b")
    FUNCTION = "map"
    CATEGORY = "🔵BB anytoany"
    
    def map(self, input_a, input_b):
        """
        将input_a映射到input_b
        直接返回两个输入值，实现任意映射
        所有输入都会被转换为字符串处理
        """
        return (str(input_a), str(input_b))


class AnyEqualsAnyString:
    """
    字符串版本的映射节点：可以将任何输入转换为字符串并映射
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_a": ("STRING", {"multiline": False, "default": ""}),
                "input_b": ("STRING", {"multiline": False, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING")
    RETURN_NAMES = ("output_a", "output_b")
    FUNCTION = "map_string"
    CATEGORY = "🔵BB anytoany"
    
    def map_string(self, input_a, input_b):
        """
        字符串映射：输入任何字符串，输出任何字符串
        """
        return (str(input_a), str(input_b))


class AnyEqualsAnyNumber:
    """
    数字版本的映射节点：可以将任何输入转换为数字并映射
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_a": ("FLOAT", {"default": 0.0, "min": -999999999, "max": 999999999, "step": 0.01}),
                "input_b": ("FLOAT", {"default": 0.0, "min": -999999999, "max": 999999999, "step": 0.01}),
            }
        }
    
    RETURN_TYPES = ("FLOAT", "FLOAT")
    RETURN_NAMES = ("output_a", "output_b")
    FUNCTION = "map_number"
    CATEGORY = "🔵BB anytoany"
    
    def map_number(self, input_a, input_b):
        """
        数字映射：输入任何数字，输出任何数字
        """
        return (float(input_a), float(input_b))


class AnyEqualsAnyUniversal:
    """
    通用映射节点：支持字符串、数字、列表等多种类型
    可以接受任意类型的输入并输出
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_a_type": (["STRING", "FLOAT", "INT"], {"default": "STRING"}),
                "input_a_value": ("STRING", {"multiline": False, "default": ""}),
                "input_b_type": (["STRING", "FLOAT", "INT"], {"default": "STRING"}),
                "input_b_value": ("STRING", {"multiline": False, "default": ""}),
            }
        }
    
    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("output_a_value", "output_a_type", "output_b_value", "output_b_type")
    FUNCTION = "map_universal"
    CATEGORY = "🔵BB anytoany"
    
    def map_universal(self, input_a_type, input_a_value, input_b_type, input_b_value):
        """
        通用映射：根据类型转换输入值
        """
        # 转换输入A
        if input_a_type == "FLOAT":
            try:
                output_a_val = str(float(input_a_value))
            except:
                output_a_val = input_a_value
        elif input_a_type == "INT":
            try:
                output_a_val = str(int(float(input_a_value)))
            except:
                output_a_val = input_a_value
        else:
            output_a_val = str(input_a_value)
        
        # 转换输入B
        if input_b_type == "FLOAT":
            try:
                output_b_val = str(float(input_b_value))
            except:
                output_b_val = input_b_value
        elif input_b_type == "INT":
            try:
                output_b_val = str(int(float(input_b_value)))
            except:
                output_b_val = input_b_value
        else:
            output_b_val = str(input_b_value)
        
        return (output_a_val, input_a_type, output_b_val, input_b_type)


class AnyTypeToAnyType:
    """
    任意值类型转换任意值类型节点
    可以将任意输入类型转换为任意输出类型
    例如：字符串"123"转换为整数123，或浮点数3.14转换为字符串"3.14"
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "input_type": (["STRING", "FLOAT", "INT"], {"default": "STRING"}),
                "input_value": ("STRING", {"multiline": False, "default": ""}),
                "output_type": (["STRING", "FLOAT", "INT"], {"default": "STRING"}),
            }
        }
    
    RETURN_TYPES = ("STRING", "FLOAT", "INT")
    RETURN_NAMES = ("output_string", "output_float", "output_int")
    FUNCTION = "convert_type"
    CATEGORY = "🔵BB anytoany"
    
    def convert_type(self, input_type, input_value, output_type):
        """
        类型转换：根据输入类型解析值，然后转换为输出类型
        """
        # 首先根据输入类型解析输入值
        parsed_value = None
        
        if input_type == "FLOAT":
            try:
                parsed_value = float(input_value)
            except:
                parsed_value = 0.0
        elif input_type == "INT":
            try:
                parsed_value = int(float(input_value))
            except:
                parsed_value = 0
        else:  # STRING
            parsed_value = str(input_value)
        
        # 然后根据输出类型转换值
        output_string = ""
        output_float = 0.0
        output_int = 0
        
        if output_type == "FLOAT":
            try:
                if isinstance(parsed_value, str):
                    output_float = float(parsed_value)
                elif isinstance(parsed_value, int):
                    output_float = float(parsed_value)
                else:
                    output_float = parsed_value
                output_string = str(output_float)
                output_int = int(output_float)
            except:
                output_float = 0.0
                output_string = str(parsed_value)
                output_int = 0
        elif output_type == "INT":
            try:
                if isinstance(parsed_value, str):
                    output_int = int(float(parsed_value))
                elif isinstance(parsed_value, float):
                    output_int = int(parsed_value)
                else:
                    output_int = parsed_value
                output_string = str(output_int)
                output_float = float(output_int)
            except:
                output_int = 0
                output_string = str(parsed_value)
                output_float = 0.0
        else:  # STRING
            output_string = str(parsed_value)
            try:
                output_float = float(parsed_value) if parsed_value else 0.0
            except:
                output_float = 0.0
            try:
                output_int = int(float(parsed_value)) if parsed_value else 0
            except:
                output_int = 0
        
        return (output_string, output_float, output_int)


# 节点映射表，用于ComfyUI自动注册
NODE_CLASS_MAPPINGS = {
    "anytoany": anytoany,
    "AnyEqualsAnyString": AnyEqualsAnyString,
    "AnyEqualsAnyNumber": AnyEqualsAnyNumber,
    "AnyEqualsAnyUniversal": AnyEqualsAnyUniversal,
    "AnyTypeToAnyType": AnyTypeToAnyType,
}

# 节点显示名称
NODE_DISPLAY_NAME_MAPPINGS = {
    "anytoany": "🔵BB 任意映射 (Any = Any)",
    "AnyEqualsAnyString": "🔵BB 字符串映射 (String = String)",
    "AnyEqualsAnyNumber": "🔵BB 数字映射 (Number = Number)",
    "AnyEqualsAnyUniversal": "🔵BB 通用映射 (Universal)",
    "AnyTypeToAnyType": "🔵BB 任意类型转换 (Any Type → Any Type)",
}

