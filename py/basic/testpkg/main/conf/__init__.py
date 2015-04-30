from collections import OrderedDict
import importlib
import os

_CONF_MODULE_ENV_VAR = 'TESTPKG_CONFIG'

class DictDotWrapper(object):
    def __init__(self, a_dict):
        object.__setattr__(self,
                        '__dict_dot_wrapper_underlying_dict__',
                        a_dict)

    def __getattr__(self, name):
        return object.__getattribute__(self,
                       '__dict_dot_wrapper_underlying_dict__')[name]

    def __setattr__(self, name, value):
        object.__getattribute__(self,
                       '__dict_dot_wrapper_underlying_dict__')[name] = value

    def __delattr__(self, name):
        del object.__getattribute__(self,
                       '__dict_dot_wrapper_underlying_dict__')[name]

    __getitem__ = __getattr__
    __setitem__ = __setattr__
    __delitem__ = __delattr__

    def settings(self):
        return object.__getattribute__(self, '__dict_dot_wrapper_underlying_dict__').keys()

    def get(self, key, default=None):
        return object.__getattribute__(self, '__dict_dot_wrapper_underlying_dict__').get(key, default)



def load_conf(module_name):
    try:
        mod = importlib.import_module(module_name)
    except ImportError as e:
        raise ImportError(
            "Could not import configuration from '%s' (Is it on sys.path? Is there an import error in the conf file?): %s"
            % (config_module, e)
        )

    config_dict = dict()
    config = DictDotWrapper(config_dict)

    for setting in dir(mod):
        setting_value = getattr(mod, setting)
        config_dict[setting] = setting_value

    return config



CONFIG = DictDotWrapper(dict())
CONFIG_MODULE_NAME = None

CONFIG_MODULE_NAME = os.environ.get(_CONF_MODULE_ENV_VAR, None)
if CONFIG_MODULE_NAME is not None:
    CONFIG = load_conf(CONFIG_MODULE_NAME)
