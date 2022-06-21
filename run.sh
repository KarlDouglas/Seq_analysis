cutadapt -b file:barcodes.fasta -o {name}.F.fastq CY001_FDDP220175289-1a_HMMLFDRXY_L1_1.fq
cutadapt -b file:barcodes.fasta -o {name}.R.fastq CY001_FDDP220175289-1a_HMMLFDRXY_L1_2.fq
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC1.F.fastq > BC1.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC1.R.fastq > BC1.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC2.F.fastq > BC2.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC2.R.fastq > BC2.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC3.F.fastq > BC3.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC3.R.fastq > BC3.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC4.F.fastq > BC4.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC4.R.fastq > BC4.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC5.F.fastq > BC5.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC5.R.fastq > BC5.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC6.F.fastq > BC6.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC6.R.fastq > BC6.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC7.F.fastq > BC7.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC7.R.fastq > BC7.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC8.F.fastq > BC8.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC8.R.fastq > BC8.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC9.F.fastq > BC9.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC9.R.fastq > BC9.R.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC10.F.fastq > BC10.F.map
/home/ptc872_alumni_ku_dk/modi_mount/bowtie/bowtie  /home/ptc872_alumni_ku_dk/modi_mount/bowtie/indexes/Leu2i  --suppress 1,2,3,6,7,8,9 BC10.R.fastq > BC10.R.map
mv BC1.F.map Seq_analysis
mv BC1.R.map Seq_analysis
mv BC2.F.map Seq_analysis
mv BC2.R.map Seq_analysis
mv BC3.F.map Seq_analysis
mv BC3.R.map Seq_analysis
mv BC4.F.map Seq_analysis
mv BC4.R.map Seq_analysis
mv BC5.F.map Seq_analysis
mv BC5.R.map Seq_analysis
mv BC6.F.map Seq_analysis
mv BC6.R.map Seq_analysis
mv BC7.F.map Seq_analysis
mv BC7.R.map Seq_analysis
mv BC8.F.map Seq_analysis
mv BC8.R.map Seq_analysis
mv BC9.F.map Seq_analysis
mv BC9.R.map Seq_analysis
cd Seq_analysis
python testrun.py