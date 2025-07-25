import os
import logging


def main():
    logger = logging.getLogger(__name__)
    # Place path of your photos for comparison
    main_path = "D:/Personal/Google Photos/"

    '''
    List directories inside the main_path Remove Archive folder name. 
    This is where we'll remove the duplicates that exist in other folders inside the main path.
    '''
    comparison_path = os.listdir(main_path)
    comparison_path.remove('Archive')
    logger.info(f"Folder list = {comparison_path}")
    archive_path = os.path.join(main_path, "Archive")

    # Initialize Logging
    logging.basicConfig(filename='dedup.log', level=logging.INFO)
    logger.info("Start duplicate removal")

    for c in comparison_path:
        path = os.path.join(main_path, c)
        print(path)
        # Traverse files in main_path
        for root, d_names, f_names in os.walk(path):
            for f in f_names:
                # Check if file with same name exists in archive_path
                if os.path.exists(os.path.join(archive_path, f)):
                    logger.info(f"Deleting {f} in {archive_path}")
                    # Delete the file inside the archive path
                    # WARNING: os.remove() permanently deletes the file and does not store it in Trash/Recycle Bin
                    os.remove(os.path.join(archive_path, f))
        print(f"Done processing: {path}")

if __name__ == '__main__':
    main()
