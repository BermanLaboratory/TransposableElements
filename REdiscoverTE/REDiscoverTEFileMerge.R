list.of.packages <- c("BiocManager")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages, repos='http://cran.us.r-project.org')

# For Bioconductor package 
list.of.packages <- c("edgeR")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) BiocManager::install(new.packages)

library('glue')

REDiscoverTEFileMerge <- function() {
  
  prj_dir_path <- list.dirs(full.names = TRUE, recursive = FALSE)
  sample_names <- list.dirs(full.names = FALSE, recursive = FALSE)
  prj_path <- getwd()
  
  type <- c('GENE', 'all', 'exon', 'intergenic', 'intron')
  lengths <- data.frame(row.names=type , val=c(57374, 15422, 4579, 10670, 11415))
  datatypes <- c('1_raw_counts', '2_counts_normalized', '3_TPM')
  
  
  for(elementType in 1:length(type)) {
    name = type[elementType]
    lengthchar = c(1:lengths[name, ])
    
    for(d in 1:length(prj_dir_path)){
      for(datatype in 1:length(datatypes)){
        
        df <- readRDS(paste0(prj_dir_path[d], glue("/result/RE_{elementType}_{datatype}.RDS")))
        df <- df$counts
        counts <- cbind(lengthchar, df)
        
        counts <- counts[,-1]
        colnames(counts) <- sample_names
        saveRDS(counts, file =paste0(prj_path, glue("/{elementType}_{datatype}.RDS")))

      }
      
    }
    
  }
  
}

REDiscoverTEFileMerge()