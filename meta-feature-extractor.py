class MFExtractor:

    def __init__(self, meta_function, obj, post_proc):
        self.meta_function = meta_function
        self.obj = obj
        self.post_proc = post_proc


    def extract(self):
        mf_result = self.meta_fuction.run(obj)
        return self.post_proc.run(mf_result)
