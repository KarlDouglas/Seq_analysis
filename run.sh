cd ..
conda config --add channels defaults
conda config --add channels bioconda
conda install cutadapt
y
cutadapt -g file:barcodes.fasta -o {name}.F.fastq CY001_F.fastq
cutadapt -g file:barcodes.fasta -o {name}.R.fastq CY001_R.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC1.F.fastq -2 BC1.R.fastq -o BC1.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC2.F.fastq -2 BC2.R.fastq -o BC2.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC3.F.fastq -2 BC3.R.fastq -o BC3.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC4.F.fastq -2 BC4.R.fastq -o BC4.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC5.F.fastq -2 BC5.R.fastq -o BC5.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC6.F.fastq -2 BC6.R.fastq -o BC6.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC7.F.fastq -2 BC7.R.fastq -o BC7.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC8.F.fastq -2 BC8.R.fastq -o BC8.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC9.F.fastq -2 BC9.R.fastq -o BC9.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/NGmerge/NGmerge -1 BC10.F.fastq -2 BC10.R.fastq -o BC10.merged.fastq
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC1.merged.fastq > BC1.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC2.merged.fastq > BC2.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC3.merged.fastq > BC3.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC4.merged.fastq > BC4.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC5.merged.fastq > BC5.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC6.merged.fastq > BC6.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC7.merged.fastq > BC7.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC8.merged.fastq > BC8.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC9.merged.fastq > BC9.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC10.merged.fastq > BC10.map
mv BC1.map Seq_analysis
mv BC2.map Seq_analysis
mv BC3.map Seq_analysis
mv BC4.map Seq_analysis
mv BC5.map Seq_analysis
mv BC6.map Seq_analysis
mv BC7.map Seq_analysis
mv BC8.map Seq_analysis
mv BC9.map Seq_analysis
mv BC10.map Seq_analysis
cd Seq_analysis
python testrun.py
