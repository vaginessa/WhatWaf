__example_payload__ = '<script>alert("test");</script>'
__type__ = "changing the payload into it's uppercase equivalent"


def tamper(payload, **kwargs):
    payload = str(payload)
    return payload.upper()