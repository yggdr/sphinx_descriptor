import inspect


class Descriptor:
    def __init__(self, default_value):
        self.default_value = default_value

    def __get__(self, instance, cls):
        if instance is None:
            return self
        try:
            return instance.__dict__[self.field_name]
        except KeyError:
            return self.default_value

    def __set__(self, instance, value):
        instance.__dict__[self.field_name] = value


class TestMeta(type):
    def __new__(cls, name, bases, namespace):
        config_fields = {name: obj
                         for name, obj in namespace.items()
                         if inspect.isdatadescriptor(obj)}
        for name, obj in config_fields.items():
            pass

        return super().__new__(cls, name, bases, namespace)


class Test(metaclass=TestMeta):
    field = Descriptor("default")
