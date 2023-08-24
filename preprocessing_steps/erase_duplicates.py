import fastdup
import argparse
import pandas as pd
import os 
import glob
import tqdm 


"""
    The purpose of this code is to 
    erase duplicates from a folder that contains the images 
    separated by folders 
    
"""

MAIN_FOLDER="data/fruits-360-original-size/fruits-360-original-size/Training/"
OUTPUT_FOLDER="data/clean_dataset"
parser=argparse.ArgumentParser()
parser.add_argument("--main_folder",type=str,default=MAIN_FOLDER)
parser.add_argument("--output-folder",type=str,default=OUTPUT_FOLDER)
args=parser.parse_args()

def get_clusters(df:pd.DataFrame, sort_by:str='count', 
                min_count:int=2, ascending:bool=False):
    """
        Arguments

    """
    # columns to aggregate
    agg_dict = {'filename': list, 'mean_distance': max, 'count': len}
    if 'label' in df.columns:
        agg_dict['label'] = list
    # filter by count
    df = df[df['count'] >= min_count]
    # group and aggregate columns
    grouped_df = df.groupby('component_id').agg(agg_dict)
    # sort
    grouped_df = grouped_df.sort_values(by=[sort_by], ascending=ascending)
    return grouped_df


def main():
    
    list_of_folders=glob.glob(f"{args.main_folder}/*")
    os.makedirs(args.output_folder,exist_ok=True)
    for folder_path in list_of_folders:

        data_dir = folder_path

        folder_name=data_dir.split("/")[-1]

        output_dir = 'fastdup_analysis'
        fd = fastdup.create(work_dir=output_dir, input_dir=data_dir)
        fd.run(ccthreshold=0.9) 
        fd.vis.duplicates_gallery()    
        connected_components_df , _ = fd.connected_components()
        print(connected_components_df.head())
        clusters_df = get_clusters(connected_components_df)
        # First sample from each cluster that is kept
        cluster_images_to_keep = []
        list_of_duplicates = []

        for cluster_file_list in clusters_df.filename:
            # keep first file, discard rest
            keep = cluster_file_list[0]
            discard = cluster_file_list[1:]
            cluster_images_to_keep.append(keep)
            list_of_duplicates.extend(discard)

        print(f"Found {len(set(list_of_duplicates))} highly similar images to discard")
        print(cluster_images_to_keep)
    return 0

if __name__=="__main__":
    main()
