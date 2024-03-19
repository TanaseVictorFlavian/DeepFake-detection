import os
from utils.name_creator import name_creator
import shutil
from utils.Classes.ImageDataset import ImageDataset
from math import floor, ceil
import csv

class DatasetCreator:

    def __init__(self,
                 datasets: list,
                 junk: dict,
                 labels : dict = {"pos": 1, "neg": 0},
                 train_ratio: list = 0.8,
                 out_root: str = "./data/"):
        """
        :datasets: list of ImageDatasets objects containing data:
        :param junk: list of ImageDatasets objects containing containing "junk" 
        :param train_ratio: The train split ratio, the rest of the data will be used for testing
        :param out_root: The path where the train/test dirs will be created
        """
        self.datasets = datasets
        self.junk = junk
        self.train_ratio = train_ratio 
        self.out_root = out_root
        self.label_dict = labels

        self.positives_samples, self.negatives_samples, self.pos_junk, self.neg_junk, self.total_pos, self.total_neg = self.analyze_data()
        
        # Lists of positive/negative datasets
        self.pos_ds = []
        self.neg_ds = []
       
        self.test_path = out_root + "test/"
        self.train_path = out_root + "train/"

        # Lists of train/test samples
        self.train_samples = []
        self.test_samples = []

        # Later will be used to create the label csv's
        self.train_labels = None
        self.test_labels = None 

        # Creates the dir evnironment
        self.init_dirs()

        # Split the data into positive/negative datasets
        self.split_data()

    def split_data(self):
        for ds in self.datasets:
            if ds.label == "pos":
                self.pos_ds.append(ds)
            else:
                self.neg_ds.append(ds)
    
    def init_dirs(self):
        # Create the train/test directories
        if not os.path.exists(self.train_path):
            os.makedirs(self.train_path)

        if not os.path.exists(self.test_path):
            os.makedirs(self.test_path)


    def analyze_data(self):

        # Calculate the number of negative/positive samples
        pos_samples = 0
        neg_samples = 0

        for ds in self.datasets:
            if ds.label == "pos":
                pos_samples += len(os.listdir(ds.path))
            else:
                neg_samples += len(os.listdir(ds.path))

        # Calculate the number of negative/positive junk samples
        pos_junk = 0
        neg_junk = 0

        for j in self.junk:
            if j.label == "pos":
                pos_junk += len(os.listdir(j.path))
            else:
                neg_junk += len(os.listdir(j.path))

        total_positives = pos_samples + pos_junk
        total_negatives = neg_samples + neg_junk

        return pos_samples, neg_samples, pos_junk, neg_junk, total_positives, total_negatives

    def manage_junk(self):
        # Since the training set will be always much bigger than the junk 
        # We could easily move all the junk to the test set
        counter = len(self.train_samples)
        for j in self.junk:
            for file in os.listdir(j.path):
                if file.endswith(".png") or file.endswith(".jpg"):
                    counter += 1
                    file_name = name_creator(counter) + ".png"
                    shutil.copy2(j.path + file, self.out_root + "train/" + file_name)
                    self.train_samples.append((file_name, self.label_dict[j.label]))

                    
    def create_train_test(self):
        
        print("Processing positive samples ...")
        self.move_data(self.pos_ds, "pos")
        print("Processing negative samples ...")
        self.move_data(self.neg_ds, "neg")
        print("Mangaing junk ...")
        self.manage_junk()

        # Create the label csv's

        header = ["image_id", "label"]
        train_csv_path = self.out_root + "train_labels.csv"
        test_csv_path = self.out_root + "test_labels.csv"

        print("Writing train labels into CSV files ...")
        self.write_labels(train_csv_path, header, self.train_samples)

        print("Writing test labels into CSV files ...")
        self.write_labels(test_csv_path, header, self.test_samples)

    def write_labels(self, path, header, data):
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)

    def move_data(self, ds, label):
        
        if label == "pos":
            train_samples = floor(self.train_ratio * self.total_pos) 
        else:
            train_samples = floor(self.train_ratio * self.total_neg)  

        # Substract the positive junk 

        non_junk_samples = train_samples - sum([x.num_samples for x in self.junk if x.label == label])

        # Calculate what percentage of the non_junk samples should be moved to train

        p = non_junk_samples * 100 / sum([x.num_samples for x in ds])
        p = ceil(p) if p - floor(p) >= 0.5 else floor(p) 
        p /= 100
        
        train_counter = len(os.listdir(self.train_path))
        test_counter = len(os.listdir(self.test_path))
        
        for sub_ds in ds:
            # Calculate the sample index where we should start moving them into test
            train_samples = floor(p * sub_ds.num_samples)

            # For a small dataset we prefer a chance to have a bigger training set
            sample_index = train_samples + \
                (sub_ds.img_seq_length - train_samples % sub_ds.img_seq_length)

            for i, file in enumerate(os.listdir(sub_ds.path)):
                if file.endswith(".png") or file.endswith(".jpg"):
                    if i < sample_index:
                        train_counter += 1
                        file_name = name_creator(train_counter) + ".png"
                        shutil.copy2(sub_ds.path + file, self.out_root + "train/" + file_name)
                        self.train_samples.append((file_name, self.label_dict[label]))
                    else:
                        test_counter += 1
                        file_name = name_creator(test_counter) + ".png"
                            
                        shutil.copy2(sub_ds.path + file,
                                    self.out_root + "test/" + file_name)
                        self.test_samples.append(
                            (file_name, self.label_dict[label]))

    