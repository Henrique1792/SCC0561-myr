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

After setup images of interest (both in db and dict directories), three possibilities
are available:

1. Dictionary generation

	`python3 myr.py genDict`
	
	Myr will generate  a new dictionary using all images inside dict directory.

2. Image Analysis

	`python3 myr.py imgAnalyse <imageName>`
	
	Myr will evaluate <imageName> using dict images - giving it's similarity
	values.

3. DB Analysis
	
	`python3 myr.py dbAnalyse `

	Myr will analyse db content and measure quality as specifications 
	determine,

