def typeBasedTransformer(**kwargs):
    transformed_kwargs = {}
    
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed_kwargs[key] = value ** 2
        elif isinstance(value, str):
            transformed_kwargs[key] = value[::-1]
        elif isinstance(value, bool):
            transformed_kwargs[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed_kwargs[key] = value[::-1]
        elif isinstance(value, dict):
            transformed_kwargs[key] = {v: k for k, v in value.items()}
        else:
            transformed_kwargs[key] = value
          
    return transformed_kwargs
