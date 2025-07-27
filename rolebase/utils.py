from functools import wraps

def required_role(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        wrapper.required_role = roles  # attach the attribute to wrapper
        print(f"[Decorator Attached] Roles required: {roles}")
        return wrapper

    return decorator
