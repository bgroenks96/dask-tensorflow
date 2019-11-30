import tensorflow as tf

if tf.__version__ >= "2.0.0":
    from .core_v2 import _start_tensorflow, start_tensorflow
else:
    from .core import _start_tensorflow, start_tensorflow

__version__ = '0.1.0'
