# Mulcahy Fellowship Project

## input: reference reads  
mine were from NCBI, here is how I got them:  
look at FMNH spreadsheet --> search fish on NCBI  
is there a mitochondrial genome available?  
yes --> go to next fish  
no --> continue to next step  
are there WGS reads?  
no --> go to next fish  
yes --> download reads from NCBI via fasterq-dump  
here's how to do that:  
...

## run mtgrasp
here's how to install it (this one is easy if i remember)  
run your reads through using this template command:
```
mtgrasp.py -r1 /home/bmogi/Mitogenome-Pipeline-Comparison/new-fish-data/lplatostomus/SRR17183797_1.fastq.gz -r2 /home/bmogi/Mitogenome-Pipeline-Comparison/new-fish-data/lplatostomus/SRR17183797_2.fastq.gz -o shortnose-gar-mtgrasp -m 2 -r /home/bmogi/Mitogenome-Pipeline-Comparison/new-fish-data/lplatostomus/gar_ref.fa
```

## run mitoz
here's how to install it (you need docker if i recall)  
mount the docker image (i'm going to need to be detailed about this part because this one isn't intuitive)  
run mtgrasp output through annotate via template command:
```
sudo docker run -v $PWD:$PWD -w $PWD --rm -it guanliangmeng/mitoz:3.6 /bin/bash

mitoz annotate --outprefix shortnose-gar-mitoz --thread_number 12 --fastafiles /home/bmogi/Mitogenome-Pipeline-Comparison/new-fish-data/lplatostomus/shortnose-gar-mtgrasp_k91_kc3.final-mtgrasp_v1.1.8-assembly.fa --species_name "Lepisosteus platostomus" --genetic_code auto --clade Chordata --profiles_dir /home/bmogi/Mitogenome-Pipeline-Comparison/mitoz_custom_db/profiles
```
the databases should be fairly robust (i didn't need to alter them), however if you want to add your own fish reads you can do it like this:
```
etc etc etc
```

## make figures
make .tre --> MEGA  
blast assembled genome and find similar species
**maybe put together a little wrapper script that formats blast output into newick**
also proksee