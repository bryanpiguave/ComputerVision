# This code is to check distribution of images per folder
# Bryan Piguave


#install.packages("dplyr")
#install.packages("argparse")

library(dplyr)
library(tools)
library(argparse)
count_images <- function(directory) {
  image_files <- dir(directory, full.names = TRUE, pattern = "\\.(jpg|jpeg|png|gif)$", ignore.case = TRUE)
  return(length(image_files))
}

# Argument parser
parser <- argparse::ArgumentParser()

parser$add_argument("--main-dir", dest = "main_dir", 
                    default="data/dataset_type_of_plants_new",
                    help = "Path to the main directory containing subdirectories")

# Parse the command-line arguments
args <- parser$parse_args()
# Get a list of subdirectories (class folders)
subdirectories <- dir(args$main_dir, full.names = TRUE)
#Count images in each subdirectory
image_counts <- sapply(subdirectories, count_images)

# Create a data frame with folder names and their respective image counts
folder_names <- basename(subdirectories)
result_data <- data.frame(Folder = folder_names, Image_Count = image_counts)

# Print the result
print(result_data)

# Showing distribution
ggplot2::ggplot(data=result_data,
                mapping=ggplot2::aes(x=Folder,y=Image_Count,fill=Folder))+
  ggplot2::geom_bar(stat="identity")+
  ggplot2::labs(title="Count of images per folder",y="Image Count")+
  ggplot2::theme_minimal() +
  ggplot2::theme(axis.text.x = ggplot2::element_text(angle = 90, hjust = 1),
                 legend.position="none")
  

  


