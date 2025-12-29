import os
import shutil

SOURCE_FOLDER = "Downloads"

# create function to organise the files
def organise_by_type (folder_path):
    try:
        for filename in os.listdir(folder_path):
            file_path=os.path.join(folder_path, filename)

            # skip directories
            if os.path.isdir(file_path):
                continue


            # get file extensions
            if "." in filename:
                extension = filename.split(".")[-1]
            else:
                extension = "others"
            
            # # robust version to get extension
            # _, extension = os.filename.splitext(filename)
            # extention = extention[1:] or "others"
        
            # create file path
            target_folder = os.path.join(folder_path, extension)

            # create a folder if does not exist
            os.makedirs(target_folder, exist_ok=True)

            # move file
            shutil.move(file_path, os.path.join(target_folder, filename))
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__=="__main__":
    organise_by_type(SOURCE_FOLDER)



