from abc import ABC

"""

Meta-features:
    1.2017 
    - Number of attributes
        (count)
    - Number of Qualitative Attributes



"""


class MetaFunction(ABC):

    def __init__(self):
        pass

    def run(self, mf_input, mf_output):
        raise NotImplementedError
