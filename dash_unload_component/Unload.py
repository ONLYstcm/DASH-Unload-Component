# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Unload(Component):
    """An Unload component.


Keyword arguments:
- id (string; required)
- close (boolean; default False)"""
    @_explicitize_args
    def __init__(self, id=Component.REQUIRED, close=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'close']
        self._type = 'Unload'
        self._namespace = 'dash_unload_component'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'close']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['id']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Unload, self).__init__(**args)
