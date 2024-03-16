class VideoDataset:
    def __init__(self, name, in_root, out_root, subdirs=None, num_bins=20, sample_size=3):
        self.name = name
        self.in_root = in_root
        self.out_root = out_root
        self.num_bins = num_bins
        self.sample_size = sample_size
        self.subdirs = subdirs
        self.in_paths = self.generate_in_paths()
        self.out_paths = self.generate_out_paths()

    def generate_in_paths(self):
        if self.subdirs is None:
            return self.in_root

        in_paths = {}
        for subdir in self.subdirs:
            in_paths[subdir] = self.in_root + self.name + "/" + subdir + "/"
        return in_paths

    def generate_out_paths(self):
        if self.subdirs is None:
            return self.out_root + self.name + "/"

        out_paths = {}
        for subdir in self.subdirs:
            out_paths[subdir] = self.out_root + self.name + "/" + subdir + "/"
        return out_paths
