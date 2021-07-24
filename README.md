# SCC0561-myr

MIR software intended as SCC0561 homework. 

### Description

This implementation focus is an Multimedia Information Retriever (MIR)
specially on images.
It'll analyse input images using an input group and output it's similarity\
within an well known db and dictionary, analysed same way

Named as Myr as wordplay for MTG creature type


![Myr token](https://repositorio.sbrauble.com/arquivos/in/magic/458120/5f4244242d05c-cyxfud-x9ou32-5f4c0f98db474e7d5ef15d4ca22d26ff.jpg)

### Usage

Dict will be generated in each execution, using db/dict/<class_name> folders
After setup images of interest (both in db and dict directories), options available:

1. DB Analysis
	
	`python3 myr.py analysis`
	
	Myr will evaluate images inside db/test 


	output is sorted classification, precision, recall, F1 measurements and confusion matrix
	associated.
3. IMG analyse content

	Execution would be
	` python3 myr.py checkImg <imgName>`

