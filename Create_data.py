import os
import shutil
import tqdm

class Create_data:
    def __init__(self, src, train_txt_path, val_txt_path, img_src='/home/u/woody8657/data/C426_Pneumothorax_preprocessed/image/preprocessed/images'):
        self.src = src
        self.train_txt_path = train_txt_path
        self.val_txt_path = val_txt_path
        self.img_src = img_src

    def make_dir(self):
        os.makedirs(self.src, exist_ok=True)
        self.train_dir = os.path.join(self.src,'train')
        self.val_dir = os.path.join(self.src,'val')
        self.annotation_dir = os.path.join(self.src,'annotations') 
        os.makedirs(self.train_dir, exist_ok=True)
        os.makedirs(self.val_dir, exist_ok=True)
        os.makedirs(self.annotation_dir, exist_ok=True)

    #from yolo txt
    def make_list(self):
        with open(self.train_txt_path) as f:
            train_list = f.readlines()
        
        with open(self.val_txt_path) as f:
            val_list = f.readlines()
    
        self.train_list = [path[-18:-5] for path in train_list]
        self.val_list = [path[-18:-5] for path in val_list]

    def copy_trian_val_imgs(self):
        self.copy_img(self.train_list, self.train_dir)
        self.copy_img(self.val_list, self.val_dir)

    def copy_img(self, list, dir):
        for pid in tqdm.tqdm(list):
            source = os.path.join(self.img_src, pid+'.png')
            destination = os.path.join(dir, pid+'.png')
            shutil.copyfile(source, destination)
           
if __name__ == '__main__':
    src = '/home/u/woody8657/data/C426_Pneumothorax_preprocessed/Pix2Seq_data'
    train_path = './train_list_coarse_review.txt'
    val_path = './valid_list_coarse_review.txt' 
    Data = Create_data(src, train_path, val_path)
    
    Data.make_dir()
    Data.make_list()
    Data.copy_trian_val_imgs()
    
    
    
      
       