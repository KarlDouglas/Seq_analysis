#! /bin/bash
cd ..
conda install -c bioconda fastq-pair
conda install -c bioconda cutadapt
conda install -c bioconda/label/cf201901 cutadapt
conda install -c bioconda fastx_toolkit
conda install -c bioconda/label/cf201901 fastx_toolkit


fastq_masker -q 25 -r N -i CY001_FDDP220175289-1a_HMMLFDRXY_L1_1.fq -o masked1.fq
fastq_masker -q 25 -r N -i CY001_FDDP220175289-1a_HMMLFDRXY_L1_2.fq -o masked2.fq
cutadapt -b file:barcodes.fasta -o {name}.F.masked1.fq
cutadapt -b file:barcodes.fasta -o {name}.R.masked2.fq

fastq_pair BC1.F.fastq BC1.R.fastq
fastq_pair BC2.F.fastq BC2.R.fastq
fastq_pair BC3.F.fastq BC3.R.fastq
fastq_pair BC4.F.fastq BC4.R.fastq
fastq_pair BC5.F.fastq BC5.R.fastq
fastq_pair BC6.F.fastq BC6.R.fastq
fastq_pair BC7.F.fastq BC7.R.fastq
fastq_pair BC8.F.fastq BC8.R.fastq
fastq_pair BC9.F.fastq BC9.R.fastq
fastq_pair BC10.F.fastq BC10.R.fastq

/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC1.F.fastq.paired.fq -2 BC1.R.fastq.paired.fq -o BC1.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC2.F.fastq.paired.fq -2 BC2.R.fastq.paired.fq -o BC2.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC3.F.fastq.paired.fq -2 BC3.R.fastq.paired.fq -o BC3.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC4.F.fastq.paired.fq -2 BC4.R.fastq.paired.fq -o BC4.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC5.F.fastq.paired.fq -2 BC5.R.fastq.paired.fq -o BC5.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC6.F.fastq.paired.fq -2 BC6.R.fastq.paired.fq -o BC6.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC7.F.fastq.paired.fq -2 BC7.R.fastq.paired.fq -o BC7.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC8.F.fastq.paired.fq -2 BC8.R.fastq.paired.fq -o BC8.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC9.F.fastq.paired.fq -2 BC9.R.fastq.paired.fq -o BC9.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC10.F.fastq.paired.fq -2 BC10.R.fastq.paired.fq -o BC10.merged.fastq

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC1.merged.fastq > BC1.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC1.F.fastq.single.fq > BC1.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC1.R.fastq.single.fq > BC1.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC2.merged.fastq > BC2.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC2.F.fastq.single.fq > BC2.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC2.R.fastq.single.fq > BC2.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC3.merged.fastq > BC3.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC3.F.fastq.single.fq > BC3.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC3.R.fastq.single.fq > BC3.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC4.merged.fastq > BC4.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC4.F.fastq.single.fq > BC4.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC4.R.fastq.single.fq > BC4.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC5.merged.fastq > BC5.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC5.F.fastq.single.fq > BC5.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC5.R.fastq.single.fq > BC5.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC6.merged.fastq > BC6.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC6.F.fastq.single.fq > BC6.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC6.R.fastq.single.fq > BC6.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC7.merged.fastq > BC7.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC7.F.fastq.single.fq > BC7.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC7.R.fastq.single.fq > BC7.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC8.merged.fastq > BC8.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC8.F.fastq.single.fq > BC8.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC8.R.fastq.single.fq > BC8.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC9.merged.fastq > BC9.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC9.F.fastq.single.fq > BC9.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC9.R.fastq.single.fq > BC9.R.map

/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC10.merged.fastq > BC10.M.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC10.F.fastq.single.fq > BC10.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC10.R.fastq.single.fq > BC10.R.map


mv BC1.F.map Seq_analysis
mv BC1.R.map Seq_analysis
mv BC1.M.map Seq_analysis
mv BC2.F.map Seq_analysis
mv BC2.R.map Seq_analysis
mv BC2.M.map Seq_analysis
mv BC3.F.map Seq_analysis
mv BC3.R.map Seq_analysis
mv BC3.M.map Seq_analysis
mv BC4.F.map Seq_analysis
mv BC4.R.map Seq_analysis
mv BC4.M.map Seq_analysis
mv BC5.F.map Seq_analysis
mv BC5.R.map Seq_analysis
mv BC5.M.map Seq_analysis
mv BC6.F.map Seq_analysis
mv BC6.R.map Seq_analysis
mv BC6.M.map Seq_analysis
mv BC7.F.map Seq_analysis
mv BC7.R.map Seq_analysis
mv BC7.M.map Seq_analysis
mv BC8.F.map Seq_analysis
mv BC8.R.map Seq_analysis
mv BC8.M.map Seq_analysis
mv BC9.F.map Seq_analysis
mv BC9.R.map Seq_analysis
mv BC9.M.map Seq_analysis
mv BC10.F.map Seq_analysis
mv BC10.R.map Seq_analysis
mv BC10.M.map Seq_analysis

cd Seq_analysis
python testrun.py