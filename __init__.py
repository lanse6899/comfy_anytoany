"""
ComfyUI 任意映射节点插件
允许将任何输入映射到任何其他输入
例如：小猫=3, 1=B, 小猫=B 等
"""

try:
    from .anytoany import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS
except ImportError:
    from anytoany import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

