from .base_model import BaseEndpointModel

class CharacterEP(BaseEndpointModel):

    def __init__(self):
        super(CharacterEP, self).__init__()
        self.endpoint = "character"