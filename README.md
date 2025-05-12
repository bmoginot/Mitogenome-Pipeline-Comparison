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
commmand
```

## run mitoz
here's how to install it (you need docker if i recall)  
mount the docker image (i'm going to need to be detailed about this part because this one isn't intuitive)  
run mtgrasp output through annotate via template command:
```
command
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